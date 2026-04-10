def interpret_clusters(data, clusters):

    cluster_map = {}

    for i, cid in enumerate(clusters):

        if cid not in cluster_map:
            cluster_map[cid] = []

        # ✅ Extract message properly
        record = data[i]

        if isinstance(record, dict):
            msg = record.get("message", "")
        else:
            msg = str(record)

        cluster_map[cid].append(msg)

    # 🔍 Interpret clusters
    meanings = {}

    for cid, msgs in cluster_map.items():

        # ✅ FIX: ensure only strings
        clean_msgs = [str(m) for m in msgs if m]

        text = " ".join(clean_msgs).lower()

        if any(word in text for word in ["money", "transfer", "account"]):
            meanings[cid] = "💰 Financial Activity"

        elif any(word in text for word in ["meet", "location", "come"]):
            meanings[cid] = "📍 Meeting / Movement"

        elif any(word in text for word in ["kill", "attack", "weapon"]):
            meanings[cid] = "⚠ Criminal Intent"

        else:
            meanings[cid] = "💬 Normal Conversation"

    return meanings