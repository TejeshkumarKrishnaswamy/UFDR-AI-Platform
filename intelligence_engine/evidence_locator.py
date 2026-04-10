def locate_evidence(data):

    evidence_found = []

    keywords = [
        "transfer", "money", "secret", "delete",
        "account", "password", "otp", "bank", "fraud"
    ]

    for record in data:

        # ✅ Extract properly
        if isinstance(record, dict):
            text = record.get("message", "").lower()
            sender = record.get("sender", "Unknown")
            time = record.get("time", "Unknown")
        else:
            text = str(record).lower()
            sender = "Unknown"
            time = "Unknown"

        # 🔍 Check keywords
        for word in keywords:
            if word in text:
                evidence_found.append({
                    "sender": sender,
                    "time": time,
                    "message": text,
                    "keyword": word
                })
                break  # avoid duplicates

    return evidence_found