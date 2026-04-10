def detect_common_location(data):

    location_counts = {}

    for record in data:

        # ✅ Extract text properly
        if isinstance(record, dict):
            text = record.get("message", "")
        else:
            text = str(record)

        text = text.lower()

        # 🔍 Location keywords
        if "warehouse" in text:
            location_counts["Warehouse"] = location_counts.get("Warehouse", 0) + 1

        elif "bank" in text:
            location_counts["Bank"] = location_counts.get("Bank", 0) + 1

        elif "office" in text:
            location_counts["Office"] = location_counts.get("Office", 0) + 1

        elif "hotel" in text:
            location_counts["Hotel"] = location_counts.get("Hotel", 0) + 1

        elif "home" in text:
            location_counts["Home"] = location_counts.get("Home", 0) + 1

    # ✅ Return most frequent location
    if location_counts:
        return sorted(location_counts.items(), key=lambda x: x[1], reverse=True)
    else:
        return [("No significant location detected", 0)]