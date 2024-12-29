# Author : Samridhi Gupta
# Date : 29-12-2024
# Project : Email Validation


# Rules for a valid email address:

# The email address should be at least 6 characters long.
# The first character must be an alphabetic letter (a-z).
# The local part (before the @) should be in lowercase letters (a-z).
# The email address must contain exactly one @ symbol.
# The @ symbol separates the local part from the domain part.
# The local part can include letters, digits (0-9), and special characters like ., _, +, and -, but it should not start or end with a special character.
# The domain part (after the @) must contain at least one dot (.).
# The dot cannot be the first or last character in the domain part.
# The domain part should consist of valid domain name characters (letters, digits, and hyphens).
# The TLD (the part after the last dot) should be at least two characters long (e.g., .com, .org).
# The email address should not contain any spaces or whitespace characters.

# Regular Expression Module(regex)
import re

email_conditions = "^[a-z]{1}[a-z0-9._%+-]{4,}@[a-z0-9.-]+\.[a-z]{2}$"

email = input("Enter your email: ")

if re.match(email_conditions,email):
    print("Email is valid")
else:
    print("Email is invalid")