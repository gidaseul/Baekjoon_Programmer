from pathlib import Path
import subprocess
from datetime import datetime, timezone, timedelta
import re

README_PATH = Path("README.md")

# =========================
# Timezone (KST)
# =========================
KST = timezone(timedelta(hours=9))


def to_kst(date_str: str) -> str:
    """
    git %cs -> YYYY-MM-DD (KST 기준)
    """
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    dt = dt.replace(tzinfo=timezone.utc).astimezone(KST)
    return dt.strftime("%Y-%m-%d")



# =========================
# Git util
# =========================

def git_last_commit(path: Path) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "log", "-1", "--format=%cs", "--", str(path)],
            stderr=subprocess.DEVNULL,
            text=True,
        ).strip()
    except Exception:
        return None


def last_commit_from_folders(folders: list[Path]) -> str:
    dates = []
    for f in folders:
        d = git_last_commit(f)
        if d:
            dates.append(d)
    return max(dates) if dates else "N/A"


# =========================
# Scan rules (네가 말한 그대로)
# =========================
def scan_codetree():
    """
    Codetree/YYYYMMDD/문제폴더
    """
    base = Path("Codetree")
    problems = []

    if base.exists():
        for day in base.iterdir():
            if day.is_dir():
                for problem in day.iterdir():
                    if problem.is_dir():
                        problems.append(problem)

    return problems


def scan_leetcode():
    """
    Leetcode/문제폴더
    """
    base = Path("Leetcode")
    return [p for p in base.iterdir() if p.is_dir()] if base.exists() else []


def scan_nested(base: Path):
    """
    백준 / SWEA / 프로그래머스
    base/레벨/문제폴더
    """
    problems = []

    if base.exists():
        for level in base.iterdir():
            if level.is_dir():
                for problem in level.iterdir():
                    if problem.is_dir():
                        problems.append(problem)

    return problems


# =========================
# Stats computation
# =========================
def compute_stats():
    stats = {}

    bj = scan_nested(Path("백준"))
    stats["Baekjoon"] = {
        "count": len(bj),
        "last": last_commit_from_folders(bj),
    }

    pg = scan_nested(Path("프로그래머스"))
    stats["Programmers"] = {
        "count": len(pg),
        "last": last_commit_from_folders(pg),
    }

    sw = scan_nested(Path("SWEA"))  # ✅ SWEA도 폴더별 집계
    stats["SWEA"] = {
        "count": len(sw),
        "last": last_commit_from_folders(sw),
    }


    ct = scan_codetree()
    stats["Codetree"] = {
        "count": len(ct),
        "last": last_commit_from_folders(ct),
    }

    lc = scan_leetcode()
    stats["LeetCode"] = {
        "count": len(lc),
        "last": last_commit_from_folders(lc),
    }

    return stats


# =========================
# README update
# =========================
def replace_block(text: str, start: str, end: str, content: str) -> str:
    return text.split(start)[0] + start + "\n" + content + "\n" + end + text.split(end)[1]


def update_readme(stats: dict):
    readme = README_PATH.read_text(encoding="utf-8")

    # --- Table ---
    table = [
        "| Platform | Problems | Last Commit |",
        "|---|---:|---|",
    ]

    total = 0
    for platform, data in stats.items():
        table.append(f"| {platform} | {data['count']} | {data['last']} |")
        total += data["count"]

    # --- Total ---
    total_md = f"**Total:** {total}"

    # --- Last auto update ---
    updated_md = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    readme = replace_block(
        readme,
        "<!-- STATS:START -->",
        "<!-- STATS:END -->",
        "\n".join(table),
    )

    readme = replace_block(
        readme,
        "<!-- TOTAL:START -->",
        "<!-- TOTAL:END -->",
        total_md,
    )

    readme = replace_block(
        readme,
        "<!-- UPDATED:START -->",
        "<!-- UPDATED:END -->",
        f"🕒 Last Auto Update: {updated_md}",
    )

    README_PATH.write_text(readme, encoding="utf-8")


# =========================
# Main
# =========================
def main():
    stats = compute_stats()
    update_readme(stats)


if __name__ == "__main__":
    main()
