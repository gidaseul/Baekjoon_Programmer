from pathlib import Path
import re
import subprocess

README_PATH = Path("README.md")

# -----------------------
# 공통 유틸
# -----------------------
def count_dirs(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for p in path.iterdir() if p.is_dir())

def last_commit_date(path: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--format=%cs", "--", str(path)],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except:
        return "-"

# -----------------------
# 플랫폼별 스캔
# -----------------------
def scan_codetree():
    """
    - Problems: 날짜 폴더 아래 문제 폴더 개수 합
    - Last Update: 가장 최신 날짜 폴더명
    """
    base = Path("Codetree")
    total = 0
    latest_date = "-"

    if base.exists():
        for day in base.iterdir():
            if day.is_dir():
                total += count_dirs(day)
                latest_date = max(latest_date, day.name)

    return total, latest_date

def scan_leetcode():
    base = Path("Leetcode")
    return count_dirs(base), last_commit_date(base)

def scan_baekjoon():
    base = Path("백준")
    total = 0
    latest = "-"

    if base.exists():
        for tier in base.iterdir():
            if tier.is_dir():
                total += count_dirs(tier)
                latest = max(latest, last_commit_date(tier))

    return total, latest

def scan_swea():
    base = Path("SWEA")
    total = 0
    latest = "-"

    if base.exists():
        for level in base.iterdir():
            if level.is_dir():
                total += count_dirs(level)
                latest = max(latest, last_commit_date(level))

    return total, latest

def scan_programmers():
    base = Path("프로그래머스")
    total = 0
    latest = "-"

    if base.exists():
        for level in base.iterdir():
            if level.is_dir():
                total += count_dirs(level)
                latest = max(latest, last_commit_date(level))

    return total, latest

# -----------------------
# README 업데이트
# -----------------------
def update_readme(stats):
    text = README_PATH.read_text(encoding="utf-8")

    for platform, (count, date) in stats.items():
        pattern = rf"(\| {platform} \|\s*)\d+(\s*\|\s*).*?(\s*\|)"
        text = re.sub(
            pattern,
            lambda m: f"{m.group(1)}{count}{m.group(2)}{date}{m.group(3)}",
            text,
        )

    README_PATH.write_text(text, encoding="utf-8")

# -----------------------
# Main
# -----------------------
def main():
    stats = {
        "Baekjoon": scan_baekjoon(),
        "Programmers": scan_programmers(),
        "SWEA": scan_swea(),
        "Codetree": scan_codetree(),
        "LeetCode": scan_leetcode(),
    }
    update_readme(stats)

if __name__ == "__main__":
    main()
