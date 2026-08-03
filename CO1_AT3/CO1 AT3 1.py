import re

# Input from user
email = input("Enter Email: ")
password = input("Enter Password: ")
mobile = input("Enter Mobile Number: ")

# Email Validation
email_pattern = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$'

# Password Validation
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!])[A-Za-z\d@#$%&!]{8,}$'

# Mobile Validation
mobile_pattern = r'^[6-9]\d{9}$'

# Email Check
if re.fullmatch(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

# Password Check
if re.fullmatch(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")

# Mobile Check
if re.fullmatch(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
