#!/usr/bin/env python3
"""
백준 제출 기록 크롤러
사용법: python crawl.py
결과:  submissions.json 저장
"""

import json
import time
import os
import sys
import urllib.parse
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()

# ── 설정 ──────────────────────────────────────────────────────────────────────
BAEKJOON_ID  = os.getenv("BAEKJOON_ID")
BAEKJOON_PW  = os.getenv("BAEKJOON_PW")
OUTPUT_FILE  = "submissions.json"
MAX_PAGES    = 0    # 0 = 전체 수집
MAX_PROBLEMS = 0    # 0 = 전체 수집

BASE_URL     = "https://www.acmicpc.net"
SOLVED_AC    = "https://solved.ac/api/v3"

DELAY        = 1.5   # 요청 사이 딜레이 (초)
BATCH_SIZE   = 100   # solved.ac 한 번에 조회할 최대 문제 수

# ── 티어 매핑 ─────────────────────────────────────────────────────────────────
TIER_NAMES = {
    0:  "Unrated",
    1:  "Bronze V",   2:  "Bronze IV",   3:  "Bronze III",   4:  "Bronze II",   5:  "Bronze I",
    6:  "Silver V",   7:  "Silver IV",   8:  "Silver III",   9:  "Silver II",   10: "Silver I",
    11: "Gold V",     12: "Gold IV",     13: "Gold III",     14: "Gold II",     15: "Gold I",
    16: "Platinum V", 17: "Platinum IV", 18: "Platinum III", 19: "Platinum II", 20: "Platinum I",
    21: "Diamond V",  22: "Diamond IV",  23: "Diamond III",  24: "Diamond II",  25: "Diamond I",
    26: "Ruby V",     27: "Ruby IV",     28: "Ruby III",     29: "Ruby II",     30: "Ruby I",
}

def tier_folder(tier_num: int) -> str:
    if 1  <= tier_num <= 5:  return "Bronze"
    if 6  <= tier_num <= 10: return "Silver"
    if 11 <= tier_num <= 15: return "Gold"
    if 16 <= tier_num <= 20: return "Platinum"
    if 21 <= tier_num <= 25: return "Diamond"
    if 26 <= tier_num <= 30: return "Ruby"
    return "Unrated"

# ── 언어 → 확장자 ─────────────────────────────────────────────────────────────
LANG_EXT = {
    'Python 3': '.py', 'PyPy3': '.py', 'Python 2': '.py', 'PyPy2': '.py',
    'C++17': '.cpp',   'C++14': '.cpp', 'C++': '.cpp',    'C': '.c',
    'Java 11': '.java','Java': '.java',
    'Kotlin': '.kt',   'JavaScript': '.js', 'TypeScript': '.ts',
    'Go': '.go',       'Rust': '.rs',   'Swift': '.swift',
    'Ruby': '.rb',     'C#': '.cs',
}

def file_ext(language: str) -> str:
    for key, ext in LANG_EXT.items():
        if key in language:
            return ext
    return '.txt'

# ── Selenium 드라이버 ─────────────────────────────────────────────────────────
def setup_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

# ── 로그인 ────────────────────────────────────────────────────────────────────
def login(driver: webdriver.Chrome) -> None:
    print("로그인 중...")
    driver.get(f"{BASE_URL}/login")
    time.sleep(2)  # 페이지 초기 로드 대기

    wait = WebDriverWait(driver, 30)

    # ID / name / CSS 순서로 시도
    id_field = None
    for selector in [
        (By.ID,   "login_user_id"),
        (By.NAME, "login_user_id"),
        (By.CSS_SELECTOR, "input[type='text']"),
    ]:
        try:
            id_field = wait.until(EC.presence_of_element_located(selector))
            break
        except Exception:
            continue

    if id_field is None:
        print(f"현재 URL: {driver.current_url}")
        print(f"페이지 제목: {driver.title}")
        raise RuntimeError("로그인 페이지에서 아이디 입력창을 찾지 못했습니다.")

    pw_field = driver.find_element(By.NAME, "login_password") if driver.find_elements(By.NAME, "login_password") \
               else driver.find_element(By.ID, "login_password")

    id_field.clear()
    id_field.send_keys(BAEKJOON_ID)
    time.sleep(0.5)
    pw_field.clear()
    pw_field.send_keys(BAEKJOON_PW)
    time.sleep(0.5)

    # 로그인 버튼 클릭
    for selector in [(By.ID, "submit_button"), (By.CSS_SELECTOR, "input[type='submit']"), (By.CSS_SELECTOR, "button[type='submit']")]:
        btns = driver.find_elements(*selector)
        if btns:
            btns[0].click()
            break

    wait.until(EC.url_changes(f"{BASE_URL}/login"))
    print(f"로그인 완료: {BAEKJOON_ID}")

# ── Selenium 쿠키 → requests 세션 ─────────────────────────────────────────────
def make_session(driver: webdriver.Chrome) -> requests.Session:
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})
    for c in driver.get_cookies():
        session.cookies.set(c["name"], c["value"], domain=c.get("domain"))
    return session

# ── 제출 목록 크롤링 (맞았습니다만) ──────────────────────────────────────────
def crawl_submissions(driver: webdriver.Chrome) -> dict:
    """
    반환: {problem_id: submission_dict}  - 문제별 가장 최근 정답 1개
    Selenium으로 로드 (JS 렌더링 필요)
    """
    print("\n제출 목록 크롤링 중...")
    best: dict = {}
    url = f"{BASE_URL}/status?user_id={BAEKJOON_ID}&result_id=4"
    visited: set = {url}
    page = 0

    while url:
        page += 1
        print(f"  페이지 {page} → {url}")
        driver.get(url)

        # 테이블 로드 대기
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#status-table tbody tr"))
            )
        except Exception:
            print("  테이블 없음 → 종료")
            break

        soup = BeautifulSoup(driver.page_source, "html.parser")

        tbody = soup.select_one("#status-table tbody")
        if not tbody:
            print("  테이블 파싱 실패 → 종료")
            break

        rows = tbody.select("tr")
        if not rows:
            break

        page_collected = 0
        for row in rows:
            cells = row.select("td")
            if len(cells) < 9:
                continue

            result_text = cells[3].get_text(strip=True)

            # 맞았습니다 아닌 행은 건너뜀 (디버그 출력만)
            if "맞았습니다" not in result_text:
                print(f"    [SKIP] 제출{cells[0].get_text(strip=True)} 결과={result_text[:10]!r}")
                continue

            submission_id = cells[0].get_text(strip=True)
            problem_id    = cells[2].get_text(strip=True)
            memory_kb     = cells[4].get_text(strip=True)
            time_ms       = cells[5].get_text(strip=True)
            language      = cells[6].get_text(strip=True).split("/")[0].strip()

            # 제출 날짜: data-timestamp (Unix) → KST ISO 변환
            time_tag = cells[8].select_one("[data-timestamp]")
            if time_tag and time_tag.get("data-timestamp"):
                ts = int(time_tag["data-timestamp"])
                dt = datetime.fromtimestamp(ts, tz=KST)
                submitted_at = dt.strftime("%Y-%m-%dT%H:%M:%S+09:00")
            else:
                submitted_at = cells[8].get_text(strip=True)
                print(f"    [DATE-WARN] 타임스탬프 없음 cell[8]: {cells[8]}")

            status = "NEW " if problem_id not in best else "DUP"
            print(f"    [{status}] 제출{submission_id} 문제{problem_id} {language} {submitted_at}")

            # status 페이지는 최신순 → 처음 만난 것이 가장 최근 정답
            if problem_id not in best:
                best[problem_id] = {
                    "submission_id": submission_id,
                    "problem_id":    problem_id,
                    "problem_title": "",
                    "language":      language,
                    "file_ext":      file_ext(language),
                    "memory_kb":     memory_kb,
                    "time_ms":       time_ms,
                    "submitted_at":  submitted_at,
                }
                page_collected += 1

        print(f"  → 이 페이지에서 신규 {page_collected}개 수집 (누적 {len(best)}개)")

        # ── 다음 페이지 (더 오래된 제출) ──
        candidates = []
        for a in soup.select("a[href]"):
            href = a["href"]
            if BAEKJOON_ID in href and "top=" in href and "result_id=4" in href:
                parsed = urllib.parse.parse_qs(urllib.parse.urlparse(href).query)
                top_val = int(parsed.get("top", [0])[0])
                full = BASE_URL + href if href.startswith("/") else href
                candidates.append((top_val, full))

        # MAX_PAGES 제한 (0 = 무제한)
        if MAX_PAGES and page >= MAX_PAGES:
            url = None
            continue

        # 이미 방문한 URL 제외 후 가장 오래된 페이지로 이동
        candidates = [(t, u) for t, u in candidates if u not in visited]
        if candidates:
            candidates.sort()
            url = candidates[0][1]
            visited.add(url)
        else:
            url = None

        time.sleep(DELAY)

    print(f"총 {len(best)}개 문제 수집")
    return best

# ── 소스 코드 추출 ────────────────────────────────────────────────────────────
def get_source_code(driver: webdriver.Chrome, submission_id: str) -> str:
    driver.get(f"{BASE_URL}/source/{submission_id}")

    # 로그인 페이지로 리다이렉트 됐는지 확인
    if "/login" in driver.current_url:
        print(f"    [CODE-ERROR] 로그인 페이지로 리다이렉트됨 - 세션 만료")
        return ""

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.codemirror-textarea"))
        )
        soup_src = BeautifulSoup(driver.page_source, "html.parser")
        textarea = soup_src.select_one("textarea.codemirror-textarea")
        if textarea:
            code = textarea.get_text()
            print(f"    [CODE] {len(code)}자 수집")
            return code
        print(f"    [CODE-WARN] textarea 비어있음")
    except Exception as e:
        print(f"    [CODE-ERROR] 소스코드 수집 실패: {e}")

    return ""

# ── 문제 설명 크롤링 (Selenium 사용) ─────────────────────────────────────────
def get_problem_info(driver: webdriver.Chrome, problem_id: str) -> dict:
    driver.get(f"{BASE_URL}/problem/{problem_id}")
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "problem_description"))
        )
    except Exception:
        print(f"    [DESC-WARN] 문제설명 로드 실패 (URL: {driver.current_url})")

    soup = BeautifulSoup(driver.page_source, "html.parser")

    def inner_html(selector: str) -> str:
        el = soup.select_one(selector)
        return el.decode_contents().strip() if el else ""

    desc = inner_html("#problem_description")
    inp  = inner_html("#problem_input")
    out  = inner_html("#problem_output")

    if desc:
        print(f"    [DESC] {len(desc)}자 수집")
    else:
        print(f"    [DESC-WARN] 문제설명 비어있음")

    return {"description": desc, "input_desc": inp, "output_desc": out}

# ── solved.ac 티어/태그 일괄 조회 ─────────────────────────────────────────────
def get_tier_bulk(problem_ids: list) -> dict:
    result = {}
    for i in range(0, len(problem_ids), BATCH_SIZE):
        batch = problem_ids[i : i + BATCH_SIZE]
        ids_str = ",".join(batch)
        try:
            resp = requests.get(
                f"{SOLVED_AC}/problem/lookup?problemIds={ids_str}",
                headers={"User-Agent": "Mozilla/5.0"},
            )
            for p in resp.json():
                pid       = str(p["problemId"])
                tier_num  = p.get("level", 0)
                tag_names = []
                for tag in p.get("tags", []):
                    ko = next(
                        (d["name"] for d in tag.get("displayNames", []) if d["language"] == "ko"),
                        tag["key"],
                    )
                    tag_names.append(ko)
                # 문제 제목 (한국어 우선, 없으면 기본 title)
                titles = p.get("titleKo", "") or p.get("title", "")
                result[pid] = {
                    "problem_title": titles,
                    "tier_num":      tier_num,
                    "tier_name":     TIER_NAMES.get(tier_num, "Unrated"),
                    "tier_folder":   tier_folder(tier_num),
                    "tags":          tag_names,
                }
        except Exception as e:
            print(f"  [경고] solved.ac 배치 {i // BATCH_SIZE + 1} 실패: {e}")
            for pid in batch:
                result[pid] = {"problem_title": pid, "tier_num": 0, "tier_name": "Unrated", "tier_folder": "Unrated", "tags": []}

        if i + BATCH_SIZE < len(problem_ids):
            time.sleep(DELAY)

    return result

# ── 메인 ─────────────────────────────────────────────────────────────────────
def main():
    if not BAEKJOON_ID or not BAEKJOON_PW:
        print("오류: .env 파일에 BAEKJOON_ID, BAEKJOON_PW를 설정해주세요.")
        sys.exit(1)

    driver = setup_driver()
    try:
        login(driver)

        # 1단계: 제출 목록 (Selenium으로 JS 렌더링 후 파싱)
        submissions = crawl_submissions(driver)

        # 2단계: 티어/태그 일괄 조회
        print("\n티어 및 태그 조회 중 (solved.ac)...")
        tier_info = get_tier_bulk(list(submissions.keys()))

        # 3단계: 소스 코드 + 문제 설명
        print("\n소스 코드 및 문제 설명 수집 중...")
        result = []
        total = len(submissions)

        for idx, (pid, sub) in enumerate(submissions.items(), 1):
            if MAX_PROBLEMS and idx > MAX_PROBLEMS:
                break

            tier = tier_info.get(pid, {"problem_title": pid, "tier_num": 0, "tier_name": "Unrated", "tier_folder": "Unrated", "tags": []})
            if tier.get("problem_title"):
                sub["problem_title"] = tier["problem_title"]

            print(f"  [{idx}/{total}] #{pid} {sub['problem_title']}")

            code = get_source_code(driver, sub["submission_id"])
            prob = get_problem_info(driver, pid)

            result.append({**sub, **tier, **prob, "code": code})

            # 중간 저장 (오류 발생 시 복구 가능)
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)

            time.sleep(DELAY)

        print(f"\n완료! {OUTPUT_FILE} 에 {len(result)}개 저장됨")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
