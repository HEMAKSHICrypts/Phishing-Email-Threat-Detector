# utils.py

def analyze_email(email):
    risk = 0
    reasons = []

    suspicious_words = ["urgent", "verify", "click", "password", "bank", "login"]

    for word in suspicious_words:
        if word in email.lower():
            risk += 15
            reasons.append(f"Suspicious word detected: {word}")

    if "http" in email or "www" in email:
        risk += 30
        reasons.append("External link detected")

    # Risk Level
    if risk > 50:
        level = "HIGH 🔴"
    elif risk > 25:
        level = "MEDIUM 🟠"
    else:
        level = "LOW 🟢"

    return risk, level, reasons


def get_advice(level):
    if "HIGH" in level:
        return [
            "Do NOT click any links",
            "Do NOT share personal information",
            "Verify sender manually"
        ]
    elif "MEDIUM" in level:
        return [
            "Be cautious",
            "Check sender email carefully"
        ]
    else:
        return [
            "Looks safe, but stay alert"
        ]