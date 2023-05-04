import requests
import sys
import datetime
import json
from typing import List
import argparse

def get_pull_requests_since_date(repo: str, access_token: str, since_date: str) -> List[dict]:
    url = f"https://api.github.com/repos/{repo}/pulls"
    headers = {"Authorization": f"token {access_token}"}
    params = {
        "state": "all",
        "sort": "created",
        "direction": "desc",
        "since": since_date,
    }

    response = requests.get(url, headers=headers, params=params)
    print("url: ", url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching pull requests: {response.status_code}")

def create_markdown_table(pull_requests: List[dict], output_file: str) -> None:
    with open(output_file, "w") as f:
        f.write("| PR ID | Title | Author | Created At |\n")
        f.write("| ----- | ----- | ------ | ---------- |\n")
        for pr in pull_requests:
            f.write(f"| {pr['number']} | [{pr['title']}]({pr['html_url']}) | {pr['user']['login']} | {pr['created_at']} |\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch pull requests from a GitHub repo since a given date and output to a markdown file.")
    parser.add_argument("--repo", help="The GitHub repository, formatted as 'username/repo'.")
    parser.add_argument("--since_date", help="The date from which to fetch pull requests (YYYY-MM-DD).")
    parser.add_argument("--access_token", help="The GitHub access token with the appropriate permissions.")
    parser.add_argument("--output_file", help="The name of the output markdown file.")

    args = parser.parse_args()

    try:
        datetime.datetime.strptime(args.since_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use 'YYYY-MM-DD'.")
        sys.exit(1)

    pull_requests = get_pull_requests_since_date(args.repo, args.access_token, args.since_date)
    create_markdown_table(pull_requests, args.output_file)
    print(f"Pull requests saved to {args.output_file}")
