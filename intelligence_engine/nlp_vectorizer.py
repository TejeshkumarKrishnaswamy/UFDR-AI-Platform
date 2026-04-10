from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(data):

    clean_msgs = []

    for record in data:

        # ✅ Extract message safely
        if isinstance(record, dict):
            text = record.get("message", "")
        else:
            text = str(record)

        text = text.strip().lower()

        # ✅ Filter useless messages
        if len(text) > 3:
            clean_msgs.append(text)

    # ❌ If no valid messages
    if len(clean_msgs) == 0:
        return None, None

    vectorizer = TfidfVectorizer(
        stop_words='english',
        max_df=0.9,
        min_df=1
    )

    try:
        X = vectorizer.fit_transform(clean_msgs)
        return X, vectorizer
    except:
        return None, None