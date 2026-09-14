import re
from pathlib import Path


def load_common_passwords():
    file_path = Path(__file__).with_name("common_passwords.txt")

    if not file_path.exists():
        return set()

    with file_path.open(encoding="utf-8") as file:
        return {
            line.strip().lower()
            for line in file
            if line.strip()
        }


COMMON_PASSWORDS = load_common_passwords()


def analyze_password_length(password):
    length = len(password)

    if length < 8:
        length_points = 0
        message = "Weak length: your password is shorter than 8 characters."
        suggestion = "Use at least 12 characters."
    elif length < 12:
        length_points = 20
        message = "Fair length: your password meets the minimum length but could be longer."
        suggestion = "Aim for at least 12 characters."
    elif length < 16:
        length_points = 35
        message = "Good length: your password has a solid length."
        suggestion = "A longer passphrase can be even stronger."
    else:
        length_points = 50
        message = "Strong length: your password is at least 16 characters long."
        suggestion = "Keep it unique and avoid predictable words or patterns."

    has_lowercase = any(character.islower() for character in password)
    has_uppercase = any(character.isupper() for character in password)
    has_number = any(character.isdigit() for character in password)
    has_symbol = any(
        not character.isalnum() and not character.isspace()
        for character in password
    )

    character_checks = []
    character_points = 0

    if has_lowercase:
        character_checks.append("✓ Contains lowercase letters")
        character_points += 10
    else:
        character_checks.append("• Add lowercase letters")

    if has_uppercase:
        character_checks.append("✓ Contains uppercase letters")
        character_points += 10
    else:
        character_checks.append("• Add uppercase letters")

    if has_number:
        character_checks.append("✓ Contains numbers")
        character_points += 10
    else:
        character_checks.append("• Add a number")

    if has_symbol:
        character_checks.append("✓ Contains symbols")
        character_points += 10
    else:
        character_checks.append("• Add a symbol, such as ! or @")

    score = length_points + character_points
    pattern_warnings = []

    lowercase_password = password.lower()
    if lowercase_password in COMMON_PASSWORDS:
        score -= 50
        pattern_warnings.append(
            "⚠ This is a commonly guessed password. Use a unique passphrase instead."
        )

    common_patterns = [
        "123",
        "234",
        "345",
        "456",
        "567",
        "678",
        "789",
        "890",
        "abc",
        "qwerty"
    ]

    if any(pattern in lowercase_password for pattern in common_patterns):
        score -= 20
        pattern_warnings.append(
            "⚠ Predictable sequence detected, such as 123, abc, or qwerty."
        )

    if re.search(r"(.)\1{3,}", password):
        score -= 20
        pattern_warnings.append(
            "⚠ Repeated characters detected, such as aaaa or 1111."
        )

    score = max(0, score)

    if score < 30:
        rating = "Weak"
    elif score < 60:
        rating = "Fair"
    elif score < 80:
        rating = "Good"
    else:
        rating = "Strong"

    return {
        "score": score,
        "rating": rating,
        "message": message,
        "suggestion": suggestion,
        "character_checks": character_checks,
        "pattern_warnings": pattern_warnings
    }