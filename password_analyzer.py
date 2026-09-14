def analyze_password_length(password):
    length = len(password)

    if length < 8:
        return {
            "score": 10,
            "message": "Weak: your password is shorter than 8 characters.",
            "suggestion": "Use at least 12 characters."
        }

    if length < 12:
        return {
            "score": 40,
            "message": "Fair: your password meets the minimum length but could be longer.",
            "suggestion": "Aim for at least 12 characters."
        }

    if length < 16:
        return {
            "score": 65,
            "message": "Good: your password has a solid length.",
            "suggestion": "A longer passphrase can be even stronger."
        }

    return {
        "score": 85,
        "message": "Strong length: your password is at least 16 characters long.",
        "suggestion": "Keep it unique and avoid predictable words or patterns."
    }