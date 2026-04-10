import webview
import subprocess
import threading
import time

def start_streamlit():
    subprocess.Popen(["streamlit", "run", "app.py"])

# start streamlit in background
threading.Thread(target=start_streamlit).start()

# wait a few seconds so server starts
time.sleep(5)

# open window
webview.create_window(
    "AI Forensic Intelligence Platform",
    "http://localhost:8501",
    width=1200,
    height=800
)

webview.start()