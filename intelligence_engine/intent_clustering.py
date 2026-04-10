from sklearn.cluster import KMeans

def detect_intent_clusters(X):
    # FIX: use shape instead of len()
    n_samples = X.shape[0]

    if n_samples < 2:
        return ["Not enough data for clustering"]

    # Adjust clusters safely
    n_clusters = min(3, n_samples)

    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)

    return kmeans.labels_