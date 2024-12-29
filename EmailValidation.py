# Author : Samridhi Gupta
# Date : 29-12-2024
# Project : Email Validation

# Regular Expression Module(regex)
import re

email_conditions = "^[a-z]{1}[a-z0-9._%+-]{4,}@[a-z0-9.-]+\.[a-z]{2}$"

email = input("Enter your email: ")

if re.match(email_conditions,email):
    print("Email is valid")
else:
    print("Email is invalid")
