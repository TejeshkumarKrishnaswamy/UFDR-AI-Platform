import re

def build_timeline(data):

    timeline = []

    for record in data:

        # ✅ Extract properly
        if isinstance(record, dict):
            message = record.get("message", "").strip()
            time = record.get("time", "").strip()
            sender = record.get("sender", "Unknown")
        else:
            message = str(record)
            time = ""
            sender = "Unknown"

        # ❌ skip empty messages
        if not message:
            continue

        # ✅ Case 1: If time exists in record
        if time and time.lower() != "unknown":
            timeline.append({
                "time": time,
                "sender": sender,
                "message": message
            })
            continue

        # ✅ Case 2: Extract time from text (fallback)
        match = re.search(r"\d{1,2}:\d{2}", message)

        if match:
            timeline.append({
                "time": match.group(),
                "sender": sender,
                "message": message
            })

    return timeline