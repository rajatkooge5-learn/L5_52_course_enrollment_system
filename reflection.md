# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without running the program. It helps detect possible bugs, security weaknesses, and style problems early, making code easier to maintain and safer to use.

## 2. What are the differences between Pylint, Bandit, and Flake8?

- Pylint checks overall code quality, naming, documentation, and potential programming errors.
- Bandit scans Python code for common security vulnerabilities and unsafe coding patterns.
- Flake8 checks Python style and formatting, including whitespace and line-length issues.

## 3. Which issues were identified and how were they fixed?

The original program used a mutable default list, a bare exception handler, unsafe `eval()`, MD5 hashing, ordinary random-number generation for an OTP, shell execution with `os.system()`, and a hardcoded registrar token. These were addressed by using `None` for the optional list, checking course IDs explicitly, validating a numeric discount rate, using SHA-256, generating OTPs with `secrets`, removing shell execution, and reading the token from an environment variable. Naming, documentation, and file handling were also improved.

## 4. What did you learn about code quality and security?

I learned that static-analysis tools detect different kinds of problems and work best when used together. Running the tools before and after changes helps verify improvements. Static analysis does not replace running and testing the program, but it makes common security and maintainability issues easier to find.

## Verification

- Pylint: 10.00/10 in `pylint_report_after.txt`.
- Bandit: no issues identified in `bandit_report_after.txt`.
- Flake8: no violations in the empty `flake8_report_after.txt`.
- The corrected program ran successfully and generated `course_roster.txt`.
