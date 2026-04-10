import subprocess
import sys

def run():
    subprocess.run([
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "app.py"

    ])

if __name__ == "__main__":
    run()

