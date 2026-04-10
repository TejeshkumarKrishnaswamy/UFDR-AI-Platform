import streamlit as st
import os
import base64
# Parser
from ufdr_parser.parser import parse_files

#  Analysis
from intelligence_engine.nlp_analysis import analyze_text
from intelligence_engine.anomaly_detection import activity_frequency
from intelligence_engine.nlp_vectorizer import vectorize_text
from intelligence_engine.intent_clustering import detect_intent_clusters
from intelligence_engine.cluster_interpreter import interpret_clusters
from intelligence_engine.behavior_anomaly_ai import detect_behavior_anomaly
from intelligence_engine.pattern_mining import detect_crime_pattern
from intelligence_engine.emotion_detection import detect_emotion
from intelligence_engine.timeline_builder import build_timeline
from intelligence_engine.location_cluster import detect_common_location
from intelligence_engine.evidence_locator import locate_evidence

# Dashboard
from dashboard.visualization import show_summary
from dashboard.network_graph import show_network
def set_bg_image():
    with open("assets/bg.png", "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(5, 10, 25, 0.85);
        z-index: -1;
    }}
    </style>
    """

    st.markdown(bg_style, unsafe_allow_html=True)
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

UPLOAD_FOLDER = "uploads"

# ---------------------------------------------------
st.set_page_config(page_title="AI UFDR Forensic Platform", layout="wide")
set_bg_image()
# ---------- MAIN TITLE (BIG) ----------
st.markdown("""
<div style="
    font-size: 42px;
    font-weight: 800;
    color: #000000;
    text-align: center;
    margin-bottom: 5px;
">
🔎 AI-Driven UFDR Digital Forensic Intelligence Platform
</div>
""", unsafe_allow_html=True)


# ---------- SUBTITLE (MEDIUM) ----------
st.markdown("""
<div style="
    font-size: 18px;
    font-weight: 600;
    color: #000000;
    text-align: center;
    margin-bottom: 25px;
">
Upload UFDR extracted files (Chats, Calls, Browser History, GPS, Accounts, Device Data)
</div>
""", unsafe_allow_html=True)


# ---------- SMALL HEADER ----------
st.markdown("""
<div style="
    font-size: 20px;
    font-weight: 600;
    color: #000000;
    margin-top: 10px;
">
📷 Crime Scene Image Analysis
</div>
""", unsafe_allow_html=True)


# ---------- FILE UPLOADER ----------
crime_image = st.file_uploader(
    "Upload Crime Scene Image",
    type=["jpg", "png", "jpeg"]
)
if crime_image:
    with open("crime_scene.jpg","wb") as f:
        f.write(crime_image.getbuffer())

    from vision_ai.crime_scene_detector import detect_objects

    objects, output = detect_objects("crime_scene.jpg")

    st.subheader("Detected Objects in Scene")
    st.write(objects)

    st.image(output, caption="Highlighted Suspicious Objects")

# Upload Section
uploaded_files = st.file_uploader(
    "Upload All UFDR Files",
    accept_multiple_files=True
)

if uploaded_files:
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    for file in uploaded_files:
        with open(os.path.join(UPLOAD_FOLDER, file.name), "wb") as f:
            f.write(file.getbuffer())

    st.success("Evidence Uploaded Successfully!")

# Button Style (INLINE CSS)
st.markdown("""
<style>
div.stButton > button {
    background-color: #ffff00 !important;
    color: #ffffff !important;
    font-weight: bold !important;
    border-radius: 10px;
}
div.stButton > button span {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

if st.button("Start Investigation"):

    # Parse Files
    data = parse_files()

    if len(data) == 0:
        st.error("No readable forensic artifacts found!")
        st.stop()

    st.header("📂 Evidence Extraction Completed")

    # ✅ ADD THIS FUNCTION
    def count_records_recursive(data):
        count = 0
        if isinstance(data, list):
            return len(data)
        elif isinstance(data, dict):
            for value in data.values():
                count += count_records_recursive(value)
        return count

    # ✅ USE THIS
    total_records = count_records_recursive(data)

    # ✅ DISPLAY CORRECT COUNT
    st.metric("📊 Total Extracted Records", total_records)


    # 1️)Suspicious Keyword Detection
    st.markdown('<div class="section-header">🚨 Suspicious Message Detection</div>', unsafe_allow_html=True)


    suspicious_results = analyze_text(data)

    if suspicious_results:
        for record, word in suspicious_results:
            st.markdown(f"""
            <div style="padding:10px; border-left:5px solid red; margin-bottom:10px;">
                <b>⚠ Keyword:</b> {word}<br>
                <b>👤 Sender:</b> {record.get('sender')}<br>
                <b>🕒 Time:</b> {record.get('time')}<br>
                <b>💬 Message:</b> {record.get('message')}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("No suspicious keywords detected")


    # 2️) Communication Behavior

    st.header("📞 Communication Activity Analysis")

    anomaly = activity_frequency(data)
    st.subheader("📊 Most Frequent Words")

    freq_words = activity_frequency(data)

    for word, count in freq_words:
        st.markdown(f"""
        <div style="padding:6px; border-left:4px solid #00e0ff; margin-bottom:6px;">
            💬 <b>{word}</b> → {count}
        </div>
        """, unsafe_allow_html=True)


    # 3️) AI Conversation Clustering

    st.header("🧠 AI Conversation Intent Clustering")

    X, vect = vectorize_text(data)

    if X is None:
        st.warning("Not enough meaningful text for clustering")
    else:
        clusters = detect_intent_clusters(X)

        meanings = interpret_clusters(data, clusters)

        for cid, meaning in meanings.items():
            st.info(f"Cluster {cid} → {meaning}")

    meanings = interpret_clusters(data, clusters)

    for cid, meaning in meanings.items():
        st.info(f"Cluster {cid} → {meaning}")


    # 4️) Behavioral Anomaly Detection (AI)
    st.header("⚠ Behavioral Anomaly Detection")

    anomalies = detect_behavior_anomaly(data)

    if anomalies:
        st.subheader("Unusual Communications Found:")
        for a in anomalies:
            st.error(a)
    else:
        st.success("No abnormal behavior detected")


    # 5️) Crime Pattern Mining

    st.header("🔍 Behavior Pattern Recognition")

    pattern = detect_crime_pattern(data)
    st.info(pattern)

    # 6️) Emotional Profiling
    st.header("💬 Emotional Tone Analysis")

    emotion = detect_emotion(data)

    # Inline CSS for JSON
    st.markdown("""
    <style>
    [data-testid="stJson"] {
        background-color: #0b1220 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    [data-testid="stJson"] * {
        color: #ffffff !important;
        font-weight: bold !important;
    }
    [data-testid="stJson"] pre {
        font-size: 16px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    for e in emotion[:20]:  # limit display
        st.markdown(f"""
        <div style="padding:10px; border-left:5px solid #00e0ff; margin-bottom:10px;">
            <b>👤 Sender:</b> {e['sender']}<br>
            <b>🕒 Time:</b> {e['time']}<br>
            <b>💬 Message:</b> {e['message']}<br>
            <b>😊 Emotion:</b> {e['emotion']} (Score: {e['score']})
        </div>
        """, unsafe_allow_html=True)

    # 7️) Timeline Reconstruction

    st.header("🕒 Activity Timeline Reconstruction")

    timeline = build_timeline(data)

    if timeline:
        for item in timeline[:20]:
            st.markdown(f"""
            <div style="padding:10px; border-left:5px solid #00ffa6; margin-bottom:10px;">
                <b>🕒 {item['time']}</b><br>
                <b>👤 {item['sender']}</b><br>
                💬 {item['message']}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.write("No timestamped activity detected")

    # 8️) Location Intelligence

    st.header("📍 Frequent Location Detection")

    loc = detect_common_location(data)


    for location, count in loc:
        st.markdown(f"""
        <div style="padding:8px; border-left:4px solid #ff9800; margin-bottom:8px;">
            📍 <b>{location}</b> — {count} mentions
        </div>
        """, unsafe_allow_html=True)

    # 9️) FORENSIC EVIDENCE LOCATOR (MOST IMPORTANT)

    st.header("🧾 Suspicious Evidence Identification")

    evidence = locate_evidence(data)

    if not evidence:
        st.markdown(
            '<div class="safe-box">No suspicious keywords detected</div>',
            unsafe_allow_html=True
        )

    else:
        for e in evidence[:30]:  # limit for UI

            st.markdown(f"""
            <div class="evidence-box">
                <b>👤 Sender:</b> {e['sender']}<br>
                <b>🕒 Time:</b> {e['time']}<br>
                <b>🔍 Keyword:</b> {e['keyword']}<br>
                <b>💬 Message:</b> {e['message']}
            </div>
            """, unsafe_allow_html=True)

    # 10) Relationship Network
    show_summary(total_records, len(suspicious_results))
