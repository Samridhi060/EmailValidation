# Email Validation Project

## Author
Samridhi Gupta

## Date
29-12-2024

## Project Overview
This project provides a simple email validation tool that checks if an email address conforms to specific rules. It utilizes regular expressions to verify the validity of the email format.

## Rules for a Valid Email Address
- The email address should be at least 6 characters long.
- The first character must be an alphabetic letter (a-z).
- The local part (before the @) should be in lowercase letters (a-z).
- The email address must contain exactly one `@` symbol.
- The `@` symbol separates the local part from the domain part.
- The local part can include letters, digits (0-9), and special characters like `.`, `_`, `+`, and `-`, but it should not start or end with a special character.
- The domain part (after the `@`) must contain at least one dot (`.`).
- The dot cannot be the first or last character in the domain part.
- The domain part should consist of valid domain name characters (letters, digits, and hyphens).
- The TLD (the part after the last dot) should be at least two characters long (e.g., `.com`, `.org`).
- The email address should not contain any spaces or whitespace characters.

## Requirements
- Python 3.x
- `re` module (included in Python standard library)

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Samridhi060/email-validation.git
   cd email-validation
   ```

2. Run the script:
   ```bash
   python email_validation.py
   ```

3. Enter an email address when prompted.

## Code Explanation
The script uses the `re` module to define a regular expression that checks the validity of the email address based on the specified rules. If the email matches the pattern, it is considered valid; otherwise, it is deemed invalid.

## Acknowledgments
- Thanks to the contributors and the Python community for their resources and support.
