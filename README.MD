# Fetch Pull Requests

This tool fetches pull requests from a GitHub repo since a given date and outputs them to a markdown file.

## Prerequisites

- Docker
- GitHub access token with the appropriate permissions

## Usage

1. Clone the repository

2. Build container
```sh
docker build -t fetch_prs .
```
3. Create a symbolic link to the `run_container.sh` script in a directory that is in your system's PATH. For example:
```sh
sudo ln -s "$(pwd)/run_container.sh" /usr/local/bin/fetch_prs
```

Make sure to replace `/usr/local/bin` with the desired directory in your system's PATH.

3. Run the tool:

```sh
fetch_prs username/repo 2023-01-01 your_access_token output.md
```


This will create a markdown file named `output.md` in the current directory with pull requests from the specified repository since January 1, 2023.
