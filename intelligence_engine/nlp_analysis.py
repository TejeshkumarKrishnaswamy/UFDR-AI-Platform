import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Forensic keyword dictionary
suspicious_keywords = [
    "kill", "murder", "bomb", "attack", "drug",
    "money transfer", "transfer", "bitcoin",
    "otp", "password", "kidnap", "meet tonight",
    "secret", "delete chat", "police", "hack",
    "fraud", "account number", "bank details"
]

def analyze_text(data):
    suspicious_found = []

    for record in data:

        # ✅ Case 1: structured data (dict)
        if isinstance(record, dict):
            message = record.get("message", "").lower()
            sender = record.get("sender", "Unknown")
            time = record.get("time", "Unknown")

        # ✅ Case 2: plain text (fallback)
        elif isinstance(record, str):
            message = record.lower()
            sender = "Unknown"
            time = "Unknown"

        else:
            continue

        # Skip very short messages
        if len(message) < 4:
            continue

        # 🔍 Check suspicious keywords
        for word in suspicious_keywords:
            if word in message:
                suspicious_found.append((
                    {
                        "sender": sender,
                        "time": time,
                        "message": message
                    },
                    word
                ))

    return suspicious_found