import os
import xml.etree.ElementTree as ET
import json
import csv

UPLOAD_FOLDER = "uploads"

def parse_files():
    extracted_data = []

    if not os.path.exists(UPLOAD_FOLDER):
        return extracted_data

    for file in os.listdir(UPLOAD_FOLDER):

        filepath = os.path.join(UPLOAD_FOLDER, file)

        try:
            # ---------------- XML ----------------
            if file.endswith(".xml"):
                tree = ET.parse(filepath)
                root = tree.getroot()

                for elem in root.iter():
                    if elem.text and elem.text.strip():
                        extracted_data.append({
                            "sender": "system",
                            "time": "unknown",
                            "message": elem.text.strip()
                        })

            # ---------------- JSON ----------------
            elif file.endswith(".json"):
                with open(filepath, encoding="utf-8") as f:
                    data = json.load(f)

                    if isinstance(data, list):
                        for item in data:
                            extracted_data.append({
                                "sender": item.get("name", "contact"),
                                "time": "unknown",
                                "message": str(item)
                            })

            # ---------------- CSV (FIXED 🔥) ----------------
            elif file.endswith(".csv"):
                with open(filepath, encoding="utf-8") as f:
                    reader = csv.reader(f)

                    headers = next(reader, None)

                    for row in reader:
                        if row:
                            extracted_data.append({
                                "sender": file,
                                "time": row[0] if len(row) > 0 else "unknown",
                                "message": " | ".join(row)
                            })

            # ---------------- TXT ----------------
            elif file.endswith(".txt"):
                with open(filepath, encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()

                    for line in lines:
                        line = line.strip()
                        if line:
                            extracted_data.append({
                                "sender": "chat",
                                "time": "unknown",
                                "message": line
                            })

        except Exception as e:
            print("Error reading:", file, e)
            continue

    return extracted_data