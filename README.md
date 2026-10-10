# Ingeri's GitHub Community Health Files

This repository contains the public GitHub profile for [@ingeri](https://github.com/ingeri) and the community-health files GitHub uses as defaults across repositories owned by this account.

## What's here

- [`profile/README.md`](profile/README.md) is the account's public profile README.
- [`CONTRIBUTING.md`](CONTRIBUTING.md), [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md), and [`SECURITY.md`](SECURITY.md) provide contribution and safety guidance.
- [`ISSUE_TEMPLATE/`](ISSUE_TEMPLATE/) contains issue intake templates for repositories that use these defaults.
- [`workflows/update-stats.yml`](workflows/update-stats.yml) refreshes the profile's public GitHub metrics every six hours and can also be run manually.
- [`scripts/update_stats.py`](scripts/update_stats.py) reads public GitHub API data and updates only the marked stats section in the profile README.

GitHub uses a public repository named `.github` for account-wide community health defaults. The profile README is published from the `profile/` directory.

## Maintaining the stats workflow

The workflow uses the built-in `GITHUB_TOKEN` and requires Actions to be allowed to write repository contents. To refresh metrics on demand, open **Actions**, choose **Refresh profile stats**, and run the workflow. The public stats cards in the profile are separately rendered by `github-readme-stats` and may be subject to that service's availability and cache.

The username is configured as `GITHUB_USERNAME` in the workflow. Update it if this repository is transferred to another GitHub account.
