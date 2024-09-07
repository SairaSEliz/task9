#!/usr/bin/env python3

import re

def validate_form():
    # Simulating form input
    phone_number = input("Enter your phone number: ").strip()
    password = input("Enter your password: ").strip()

    # Password validation regex (similar to the JavaScript one)
    password_regex = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).{8,}$"

    # Validate phone number
    if len(phone_number) != 10 or not phone_number.isdigit():
        print("Please enter a valid 10-digit phone number.")
        return False

    # Validate password
    if not re.match(password_regex, password):
        print("Password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return False

    # If validation passes
    print("Form submitted successfully!")
    return True

if __name__ == "__main__":
    validate_form()