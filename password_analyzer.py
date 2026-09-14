def analyze_password_length(password):
    length = len(password)

    if length < 8:
        score = 10
        message = "Weak length: your password is shorter than 8 characters."
        suggestion = "Use at least 12 characters."
    elif length < 12:
        score = 40
        message = "Fair length: your password meets the minimum length but could be longer."
        suggestion = "Aim for at least 12 characters."
    elif length < 16:
        score = 65
        message = "Good length: your password has a solid length."
        suggestion = "A longer passphrase can be even stronger."
    else:
        score = 85
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

    if has_lowercase:
        character_checks.append("✓ Contains lowercase letters")
    else:
        character_checks.append("• Add lowercase letters")

    if has_uppercase:
        character_checks.append("✓ Contains uppercase letters")
    else:
        character_checks.append("• Add uppercase letters")

    if has_number:
        character_checks.append("✓ Contains numbers")
    else:
        character_checks.append("• Add a number")

    if has_symbol:
        character_checks.append("✓ Contains symbols")
    else:
        character_checks.append("• Add a symbol, such as ! or @")

    return {
        "score": score,
        "message": message,
        "suggestion": suggestion,
        "character_checks": character_checks
    }