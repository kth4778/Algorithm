#!/usr/bin/env python3
"""
submissions.json → 날짜 지정 git commit
사용법: python commit.py
주의:  push는 직접 해야 함 (git push)
"""

import json
import os
import re
import subprocess
import sys

from dotenv import load_dotenv

load_dotenv()

REPO_PATH   = os.getenv("REPO_PATH", os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE  = "submissions.json"

# Windows 파일명에 사용할 수 없는 문자 → 대체 문자
INVALID_CHARS = re.compile(r'[\\/:*?"<>|]')

def sanitize_name(name: str) -> str:
    """파일/폴더명에 쓸 수 없는 문자 제거. + → ＋ (BaekjoonHub 방식)"""
    name = name.replace("+", "＋")
    name = INVALID_CHARS.sub("", name)
    return name.strip()

# ── README.md 생성 ────────────────────────────────────────────────────────────
def format_date(iso: str) -> str:
    """2026-03-24T22:31:09+09:00 → 2026년 3월 24일 22:31:09"""
    try:
        from datetime import datetime, timezone, timedelta
        KST = timezone(timedelta(hours=9))
        dt = datetime.fromisoformat(iso)
        return dt.strftime(f"{dt.year}년 {dt.month}월 {dt.day}일 %H:%M:%S")
    except Exception:
        return iso

def build_readme(sub: dict) -> str:
    tags_str = ", ".join(sub.get("tags", [])) or "없음"
    return f"""# [{sub['tier_name']}] {sub['problem_title']} - {sub['problem_id']}

[문제 링크](https://www.acmicpc.net/problem/{sub['problem_id']})

### 성능 요약

메모리: {sub['memory_kb']} KB, 시간: {sub['time_ms']} ms

### 분류

{tags_str}

### 제출 일자

{format_date(sub['submitted_at'])}

### 문제 설명

{sub.get('description', '')}

### 입력

{sub.get('input_desc', '')}

### 출력

{sub.get('output_desc', '')}
"""

# ── git 명령 실행 헬퍼 ────────────────────────────────────────────────────────
def git(args: list, env: dict = None) -> subprocess.CompletedProcess:
    base_env = os.environ.copy()
    if env:
        base_env.update(env)
    return subprocess.run(
        ["git"] + args,
        cwd=REPO_PATH,
        env=base_env,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )

# ── 메인 ─────────────────────────────────────────────────────────────────────
def main():
    if not os.path.exists(INPUT_FILE):
        print(f"오류: {INPUT_FILE} 파일이 없습니다. 먼저 crawl.py를 실행하세요.")
        sys.exit(1)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        submissions: list = json.load(f)

    print(f"총 {len(submissions)}개 처리 시작\n")
    committed = 0
    skipped   = 0

    for sub in submissions:
        pid    = sub["problem_id"]
        title  = sanitize_name(sub["problem_title"])
        folder = sub.get("tier_folder", "Unrated")
        ext    = sub.get("file_ext", ".py")
        date   = sub["submitted_at"]

        # ── 폴더 경로 ──
        problem_dir = os.path.join(REPO_PATH, "백준", folder, f"{pid}. {title}")

        # 이미 존재하면 건너뜀
        if os.path.isdir(problem_dir):
            print(f"  [SKIP] #{pid} {title} (이미 존재)")
            skipped += 1
            continue

        print(f"  [COMMIT] #{pid} {title} ({date})")

        # ── 파일 생성 ──
        os.makedirs(problem_dir, exist_ok=True)

        code_path   = os.path.join(problem_dir, f"{title}{ext}")
        readme_path = os.path.join(problem_dir, "README.md")

        with open(code_path, "w", encoding="utf-8") as f:
            f.write(sub.get("code", ""))

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(build_readme(sub))

        # ── git add ──
        rel_dir = os.path.relpath(problem_dir, REPO_PATH).replace("\\", "/")
        add_result = git(["add", rel_dir])
        if add_result.returncode != 0:
            print(f"    [오류] git add 실패: {add_result.stderr}")
            continue

        # ── git commit (날짜 지정) ──
        commit_msg = (
            f"[{sub['tier_name']}] "
            f"Title: {sub['problem_title']}, "
            f"Time: {sub['time_ms']} ms, "
            f"Memory: {sub['memory_kb']} KB"
        )
        commit_result = git(
            ["commit", "-m", commit_msg],
            env={
                "GIT_AUTHOR_DATE":    date,
                "GIT_COMMITTER_DATE": date,
            },
        )
        if commit_result.returncode == 0:
            committed += 1
        else:
            print(f"    [오류] git commit 실패: {commit_result.stderr}")

    print(f"\n완료: {committed}개 커밋, {skipped}개 건너뜀")
    print("push하려면: git push")


if __name__ == "__main__":
    main()
