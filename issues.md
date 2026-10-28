# Lab 5: Static Code Analysis — Issues and Fixes

Line numbers refer to the original `course_enrollment_system.py` before fixes.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Mutable default argument | Bug | 15 | `audit_trail=[]` creates a shared mutable default that can retain values across calls. | Changed the default to `None` and initialized the list inside the function. |
| Broad exception handler | Code quality | 27–32 | A bare `except` hides unexpected errors. | Removed the broad handler and checked whether the course ID exists. |
| Unsafe `eval()` | Security (Bandit B307) | 45–47 | Evaluating a string can execute unintended Python expressions. | Replaced expression evaluation with a numeric discount rate and validated its range. |
| Weak MD5 hash | Security (Bandit B324) | 51–52 | MD5 is unsuitable for modern security-sensitive hashing. | Replaced MD5 with SHA-256. |
| Insecure OTP generator | Security (Bandit B311) | 55–56 | Ordinary pseudo-random generation is unsuitable for security-sensitive tokens. | Used the `secrets` module. |
| Shell command execution | Security (Bandit B605) | 59–63 | `os.system()` starts a shell unnecessarily and can introduce command-injection risk. | Removed shell execution and printed the export message directly. |
| Hardcoded registrar token | Security (Bandit B105) | 74–75 | A fixed secret was embedded in source code. | Read the token from the `REGISTRAR_AUTH_TOKEN` environment variable and never print the secret itself. |
| Naming and missing docstrings | Code quality (Pylint) | Multiple | Function names did not use snake_case and functions lacked documentation. | Renamed functions and added docstrings. |
| Unused imports and variables | Code quality (Pylint / Flake8) | 4, 36, 46, 68 | Unused code produced warnings and reduced maintainability. | Removed unused imports and variables and simplified functions. |
| File handling and formatting | Code quality (Pylint / Flake8) | 60–63 and multiple | File encoding was implicit, the file was closed manually, and some lines were too long. | Used a context manager with UTF-8 encoding and formatted long lines. |

## Verification Results

- Pylint: 10.00/10 (recorded in `pylint_report_after.txt`).
- Bandit: no issues identified (recorded in `bandit_report_after.txt`).
- Flake8: the after-report is empty, indicating no reported violations.
- Program: ran successfully and generated `course_roster.txt`.

The before reports preserve results from the original version. The after reports record the checks after the fixes.
