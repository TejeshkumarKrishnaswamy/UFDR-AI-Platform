from collections import Counter
import re

def activity_frequency(data):

    words_list = []

    stop_words = [
        "the","is","and","to","a","in","of","for","on","at","with",
        "ok","yes","no","hi","hello","are","you","i","am"
    ]

    for record in data:

        # ✅ Extract only message
        if isinstance(record, dict):
            text = record.get("message", "")
        else:
            text = str(record)

        text = text.lower()

        # ❌ Remove dates, numbers, special chars
        text = re.sub(r'\d+', '', text)  # remove numbers
        text = re.sub(r'[^a-z\s]', '', text)  # keep only words

        words = text.split()

        for word in words:
            if len(word) > 3 and word not in stop_words:
                words_list.append(word)

    # ✅ Count frequency
    freq = Counter(words_list)

    return freq.most_common(10)