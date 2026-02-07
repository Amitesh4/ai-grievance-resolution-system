from datetime import datetime, timedelta


def classify_department(text: str) -> str:
    text = text.lower()

    if "water" in text or "pipe" in text:
        return "Water Department"
    if "road" in text or "pothole" in text:
        return "Roads Department"
    if "electric" in text or "power" in text:
        return "Electricity Department"
    if "garbage" in text or "waste" in text:
        return "Sanitation Department"

    return "General Administration"


def detect_priority(text: str) -> str:
    text = text.lower()

    if "accident" in text or "fire" in text or "hospital" in text:
        return "High"
    if "not working" in text or "broken" in text:
        return "Medium"

    return "Low"


def assign_sla(priority: str) -> str:
    now = datetime.utcnow()

    if priority == "High":
        deadline = now + timedelta(hours=24)
    elif priority == "Medium":
        deadline = now + timedelta(days=3)
    else:
        deadline = now + timedelta(days=7)

    return deadline.isoformat()
