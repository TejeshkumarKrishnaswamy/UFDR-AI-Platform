from textblob import TextBlob

def detect_emotion(data):

    results = []

    for record in data:

        # ✅ Extract message safely
        if isinstance(record, dict):
            text = record.get("message", "")
            sender = record.get("sender", "Unknown")
            time = record.get("time", "Unknown")
        else:
            text = str(record)
            sender = "Unknown"
            time = "Unknown"

        if not text or len(text.strip()) < 3:
            continue

        # ✅ Sentiment analysis
        polarity = TextBlob(text).sentiment.polarity

        # 🎯 Label emotion
        if polarity > 0:
            emotion = "Positive 🙂"
        elif polarity < 0:
            emotion = "Negative ⚠"
        else:
            emotion = "Neutral 😐"

        results.append({
            "sender": sender,
            "time": time,
            "message": text,
            "emotion": emotion,
            "score": round(polarity, 2)
        })

    return results