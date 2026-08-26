# SauceDemo Playwright tests

## Run locally

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python -m pytest
```

On Windows PowerShell, replace `.venv/bin/python` with `.venv\\Scripts\\python.exe`.

## Jenkins

This repository includes a declarative `Jenkinsfile` for a Linux Jenkins agent.
The agent needs Python 3, internet access to PyPI and the Playwright browser download
servers, and permission to install the Linux dependencies required by
`playwright install --with-deps` (commonly by running the agent as a container or
as a user with passwordless `sudo`).

Create a **Pipeline** job, choose **Pipeline script from SCM**, configure the Git
repository and branch, and set the script path to `Jenkinsfile`. Jenkins will publish
the pytest result as JUnit data and archive Playwright failure traces, screenshots,
and videos from `test-results`.
