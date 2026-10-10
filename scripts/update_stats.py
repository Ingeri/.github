"""Refresh public GitHub metrics in the profile README."""

import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


USERNAME = os.environ.get("GITHUB_USERNAME", "ingeri")
README_PATH = Path(__file__).resolve().parents[1] / "profile" / "README.md"
START_MARKER = "<!-- github-stats:start -->"
END_MARKER = "<!-- github-stats:end -->"


def get_json(url: str) -> dict | list:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-profile-stats-updater",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = Request(url, headers=headers)
    with urlopen(request, timeout=20) as response:
        return json.load(response)


def collect_metrics() -> dict[str, int]:
    profile = get_json(f"https://api.github.com/users/{USERNAME}")
    if not isinstance(profile, dict):
        raise ValueError("GitHub returned an unexpected user response")

    repositories = []
    page = 1
    while True:
        result = get_json(
            f"https://api.github.com/users/{USERNAME}/repos"
            f"?type=owner&per_page=100&page={page}"
        )
        if not isinstance(result, list):
            raise ValueError("GitHub returned an unexpected repositories response")
        if not result:
            break
        repositories.extend(result)
        page += 1

    original_repositories = [repo for repo in repositories if not repo.get("fork")]
    return {
        "repositories": int(profile.get("public_repos", 0)),
        "followers": int(profile.get("followers", 0)),
        "stars": sum(int(repo.get("stargazers_count", 0)) for repo in original_repositories),
        "forks": sum(int(repo.get("forks_count", 0)) for repo in original_repositories),
    }


def format_stats(metrics: dict[str, int]) -> str:
    labels = (
        ("Public repositories", "repositories"),
        ("Followers", "followers"),
        ("Stars on original repositories", "stars"),
        ("Forks on original repositories", "forks"),
    )
    rows = ["| Metric | Count |", "| :--- | ---: |"]
    rows.extend(
        f"| {label} | {metrics[key]:,} |" for label, key in labels
    )
    return "\n".join(rows)


def update_readme(metrics: dict[str, int]) -> None:
    content = README_PATH.read_text(encoding="utf-8")
    if content.count(START_MARKER) != 1 or content.count(END_MARKER) != 1:
        raise ValueError("Profile README must contain exactly one pair of stats markers")

    start = content.index(START_MARKER) + len(START_MARKER)
    end = content.index(END_MARKER)
    if start > end:
        raise ValueError("Profile README stats markers are out of order")

    updated = content[:start] + "\n\n" + format_stats(metrics) + "\n" + content[end:]
    if updated != content:
        README_PATH.write_text(updated, encoding="utf-8")
        print("Updated profile metrics.")
    else:
        print("Profile metrics are already current.")


def main() -> None:
    try:
        update_readme(collect_metrics())
    except (HTTPError, URLError, TimeoutError, ValueError, OSError) as error:
        raise SystemExit(f"Could not refresh GitHub stats: {error}") from error


if __name__ == "__main__":
    main()