# Algorithm Project - Claude 가이드

## 프로젝트 개요
백준 알고리즘 문제 풀이 저장소. BaekjoonHub 확장 프로그램으로 자동 업로드된 구조를 따름.

## 파일 구조 (백준)

```
백준/
├── Bronze/
│   └── {문제번호}. {문제제목}/
│       ├── {문제제목}.py       # 풀이 코드
│       ├── README.md           # 문제 설명 (BaekjoonHub 자동 생성)
│       ├── input.txt           # 예제 입력
│       └── output.txt          # 예제 출력 (복수 케이스 시 input1.txt, input2.txt ...)
├── Silver/
│   └── {문제번호}. {문제제목}/
│       ├── {문제제목}.py
│       └── README.md
└── Gold/
    └── {문제번호}. {문제제목}/
        ├── {문제제목}.py
        └── README.md
```

**참고**: Bronze 폴더에는 input/output txt 파일이 있고, Silver/Gold는 없을 수 있음.

## 커밋 방식
- 과거 문제들을 올릴 때 **커밋 날짜를 원래 풀었던 날짜로 반영**해서 올림
- `GIT_AUTHOR_DATE`, `GIT_COMMITTER_DATE` 환경변수로 날짜 지정

## 작업 범위
- 백준만 진행 (프로그래머스 제외)
