
# Lab 5: Static Code Analysis — Issues and Fixes

| Issue | Tool | Fix applied |
|---|---|---|
| Unsafe eval() | Bandit | Replaced expression evaluation with validated numeric discount input |
| Weak MD5 hash | Bandit | Replaced MD5 with SHA-256 |
| Insecure OTP generation | Bandit | Used the secrets module |
| Hardcoded registrar token | Security review | Read token from an environment variable |
| Shell command execution | Bandit | Removed os.system() and used print() |
| Mutable default list | Pylint | Replaced [] with None and initialized inside the function |
| Missing docstrings | Pylint | Added module and function documentation |
| Naming convention violations | Pylint | Used snake_case for functions and uppercase constants |
| Unused imports and variables | Pylint | Removed unused imports and variables |
| File handling and encoding | Pylint | Used with open() and explicit UTF-8 encoding |
| Whitespace and formatting | Flake8 | Corrected formatting and blank-line issues |

## Verification

- Pylint: 10.00/10
- Bandit: No issues identified
- Flake8: No violations reported
- Program: Runs successfully
