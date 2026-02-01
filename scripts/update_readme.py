from pathlib import Path
import subprocess
from datetime import datetime
import re

README_PATH = Path("README.md")

PLATFORMS = {
    "Baekjoon": Path("백준"),
    "Programmers": Path("프로그래머스"),
    "SWEA": Path("SWEA"),
    "Codetree": Path("Codetree"),
    "LeetCode": Path("Leetcode"),
}

# ---------- 공통 유틸 ----------

def count_dirs(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for p in path.iterdir() if p.is_dir())

def count_codetree():
    base = Path("Codetree")
    total = 0
    if base.exists():
        for day in base.iterdir():
            if day.is_dir():
                total += count_dirs(day)
    return total

def last_commit_date(path: Path) -> str:
    try:
        date = subprocess.check_output(
            ["git", "log", "-1", "--format=%cs", "--", str(path)],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
        return date
    except:
        return "N/A"

# ---------- 스캔 ----------

def scan_stats():
    rows = []
    total = 0

    for name, path in PLATFORMS.items():
        if not path.exists():
            continue

        if name == "Codetree":
            count = count_codetree()
        else:
            count = count_dirs(path)

        last = last_commit_date(path)
        rows.append((name, count, last))
        total += count

    return rows, total

# ---------- README 업데이트 ----------

def update_readme():
    rows, total = scan_stats()
    now_utc = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    table = [
        "| Platform | Problems | Last Commit |",
        "|---|---:|---|",
    ]
    for name, cnt, last in rows:
        table.append(f"| {name} | {cnt} | {last} |")

    text = README_PATH.read_text(encoding="utf-8")

    def replace_block(start, end, content):
        nonlocal text
        text = re.sub(
            rf"{start}.*?{end}",
            f"{start}\n{content}\n{end}",
            text,
            flags=re.S,
        )

    replace_block(
        "<!-- STATS:START -->",
        "<!-- STATS:END -->",
        "\n".join(table) + f"\n\n**Total:** {total}",
    )

    replace_block(
        "<!-- UPDATED:START -->",
        "<!-- UPDATED:END -->",
        f"🕒 Last Auto Update: {now_utc}",
    )

    README_PATH.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    update_readme()
