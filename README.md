# Ingeri GitHub Community Files

This repository holds the public GitHub profile for [@ingeri](https://github.com/ingeri) and the default community health files GitHub applies across repositories owned by this account.

## Contents

- [profile/README.md](profile/README.md) — the public GitHub profile landing page.
- [CONTRIBUTING.md](CONTRIBUTING.md) — community contribution process and expectations.
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — expected behavior and reporting guidance.
- [SECURITY.md](SECURITY.md) — vulnerability disclosure practices.
- [ISSUE_TEMPLATE/](ISSUE_TEMPLATE/) — issue forms and templates for repository maintenance.
- [workflows/update-stats.yml](workflows/update-stats.yml) — automation that refreshes the profile stats on a schedule.
- [scripts/update_stats.py](scripts/update_stats.py) — script used to update the generated GitHub metrics section in the profile README.

GitHub automatically uses a repository named `.github` for account-level defaults, and the profile README is published from the [profile/](profile/) directory.

## Profile automation

The stats workflow uses the built-in `GITHUB_TOKEN` and requires repository write permissions for GitHub Actions. To refresh metrics manually:

1. Open the repository's **Actions** tab.
2. Select **Refresh profile stats**.
3. Run the workflow manually.

The profile cards shown on the page are rendered by the public GitHub stats service and may occasionally be delayed or unavailable depending on that external provider.

The username used by the automation is configured as `GITHUB_USERNAME` in [workflows/update-stats.yml](workflows/update-stats.yml). Update it when the repository is moved to a different GitHub account.
