from sklearn.ensemble import IsolationForest
import numpy as np

def detect_behavior_anomaly(messages):

    # feature extraction
    lengths = [len(m) for m in messages]

    # convert to ML format
    X = np.array(lengths).reshape(-1,1)

    model = IsolationForest(contamination=0.25, random_state=42)
    model.fit(X)

    prediction = model.predict(X)

    anomalies = []

    for i, p in enumerate(prediction):
        if p == -1:
            anomalies.append(messages[i])

    return anomalies
