# Lab 5: Static Code Analysis — Issues and Fixes

Line numbers below refer to the original `course_enrollment_system.py`, before fixes.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Mutable default argument | Bug / code quality | 15 | The default `audit_trail=[]` can retain a shared list across calls. | Changed the default to `None` and initialize a list inside the function. |
| Broad exception handler | Code quality | 31–32 | A bare `except` hides errors that should be handled explicitly. | Removed the broad exception handler and checked whether the course ID exists. |
| Unsafe `eval()` | Security (Bandit B307) | 47 | Evaluating a string can execute unintended Python expressions. | Replaced expression evaluation with a numeric discount rate and range validation. |
| Weak MD5 hash | Security (Bandit B324) | 52 | MD5 is not appropriate for modern security-sensitive digest use. | Replaced MD5 with SHA-256. |
| Insecure OTP random generator | Security (Bandit B311) | 56 | The ordinary pseudo-random generator is not designed for security tokens. | Used the `secrets` module to generate the OTP. |
| Shell command execution | Security (Bandit B605) | 63 | `os.system()` starts a shell unnecessarily and may create command-injection risk. | Removed shell execution and printed the export message directly. |
| Hardcoded registrar token | Security (Bandit B105) | 75 | A fixed secret is embedded in source code. | Read the token from the `REGISTRAR_AUTH_TOKEN` environment variable and do not print its value. |
| Naming and missing docstrings | Code quality (Pylint) | Multiple | Function names did not use snake_case and functions lacked documentation. | Renamed functions to snake_case and added docstrings. |
| Unused import and variable | Code quality (Pylint / Flake8) | 4, 36, 46, 68 | Unused code made the program harder to maintain and produced warnings. | Removed unused imports/variables and simplified the relevant functions. |
| File handling and formatting | Code quality (Pylint / Flake8) | 60–63 and multiple | The file was opened without an explicit encoding and closed manually; several lines exceeded style limits. | Used a context manager with UTF-8 encoding and formatted long lines. |

## Verification Results

- Pylint: 10.00/10 (from `pylint_report_after.txt`).
- Bandit: no issues identified (from `bandit_report_after.txt`).
- Flake8: the after-report is empty, indicating no reported violations.
- Program: ran successfully and generated `course_roster.txt`.

The before reports preserve the findings from the original version; the after reports record the checks after fixes.
