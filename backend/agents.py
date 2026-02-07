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
