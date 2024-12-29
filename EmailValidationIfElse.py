# Author : Samridhi Gupta
# Date : 29-12-2024
# Project : Email Validation

email = input("Enter your email: ")

# Check the basic conditions for a valid email
if len(email) >= 6:
    if email[0].isalpha() and email.islower():
        if "@" in email and email.count("@") == 1:
            local_part, domain_part = email.split("@")
            if '.' in domain_part and domain_part.index('.') > 0 and domain_part[-1] != '.':
                print("Email is valid")
            else:
                print("Email is not valid")
        else:
            print("Email is not valid")
    else:
        print("Email is not valid")
else:
    print("Email is not valid")
