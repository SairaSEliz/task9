#!/usr/bin/env python3
from flask import Flask, request, jsonify, render_template_string
import re

app = Flask(__name__)

def validate_form(phone_number, email):
    # Validate phone number
    if len(phone_number) != 10 or not phone_number.isdigit():
        return "Please enter a valid 10-digit phone number."

    # Validate email format
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return "Please enter a valid email address."

    # If validation passes
    return None

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    phone_number = request.form.get('phone_number')  # Assuming phone_number is also in the form

    error_message = validate_form(phone_number, email)

    if error_message:
        return jsonify({"error": error_message}), 400

    # Process the form data (e.g., save to a database or send an email)
    return jsonify({"message": "Form submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
