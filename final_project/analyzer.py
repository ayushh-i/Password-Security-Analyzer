import re
import math

def analyze_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers")

    # Special characters
    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Entropy calculation
    charset_size = 94
    entropy = len(password) * math.log2(charset_size)

    # Strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, round(entropy, 2), feedback