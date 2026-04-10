import streamlit as st

def show_summary(total_records, suspicious_count):

    st.header("📊 Forensic Summary")

    col1, col2 = st.columns(2)

    col1.metric("Total Extracted Records", total_records)
    col2.metric("Suspicious Indicators", suspicious_count)

    if suspicious_count > 5:
        st.error("⚠ HIGH RISK USER BEHAVIOR DETECTED")
    elif suspicious_count > 0:
        st.warning("⚠ Moderate Suspicion Detected")
    else:
        st.success("No suspicious behavioral evidence")
