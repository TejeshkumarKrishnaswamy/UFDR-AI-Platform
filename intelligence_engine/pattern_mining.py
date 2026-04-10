def detect_crime_pattern(data):

    suspicious_patterns = []

    for record in data:

        # ✅ Extract message safely
        if isinstance(record, dict):
            text = record.get("message", "")
        else:
            text = str(record)

        text = text.lower()

        # 🔍 Pattern rules
        if "transfer" in text and "money" in text:
            suspicious_patterns.append("💰 Financial Transaction Pattern Detected")

        elif "meet" in text and "location" in text:
            suspicious_patterns.append("📍 Secret Meeting Pattern Detected")

        elif "delete" in text or "clear chat" in text:
            suspicious_patterns.append("🧹 Evidence Deletion Behavior Detected")

        elif "otp" in text or "password" in text:
            suspicious_patterns.append("🔐 Sensitive Information Sharing Detected")

        elif "late night" in text or "midnight" in text:
            suspicious_patterns.append("🌙 Unusual Time Communication Pattern")

    # ✅ Remove duplicates
    if suspicious_patterns:
        return list(set(suspicious_patterns))
    else:
        return ["No suspicious pattern found"]