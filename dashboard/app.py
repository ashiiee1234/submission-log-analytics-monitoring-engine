import os
import sys

import streamlit as st
import plotly.express as px

# Ensure project root is on sys.path so 'backend' is importable
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from backend.processing.pipeline import build_pipeline
from backend.anomaly.detecter import detect_anomaly
from backend.config.email_config import send_log_report


st.title("Python Based High Throughput Log Analytics Monitoring Engine")

# Log file: use sample_log.log (parser expects space-separated lines, not CSV)
log_path = os.path.join(PROJECT_ROOT, "backend", "data", "sample_log.log")

log_df = build_pipeline(log_path)
log_pd = log_df.compute()

# Normalize level to uppercase for consistent grouping (sample has "info" and "INFO")
log_pd = log_pd.copy()
log_pd["level"] = log_pd["level"].astype(str).str.upper()

# --- Log Level Distribution (Pie Chart) ---
st.subheader("Log Level Distribution")
st.caption("Distribution of Log Levels")
level_counts = log_pd["level"].value_counts()
if not level_counts.empty:
    fig_pie = px.pie(
        values=level_counts.values,
        names=level_counts.index,
        title="Log Level Distribution",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    st.plotly_chart(fig_pie)
else:
    st.info("No log levels to display.")

# --- Log Levels Over Time (Line Chart) ---
st.subheader("Log Levels Over Time")
st.caption("Log Level Timeline")
# Map level to numeric for line plot (INFO=0, WARN=1, ERROR=2)
level_order = {"INFO": 0, "WARN": 1, "ERROR": 2}
log_pd["level_num"] = log_pd["level"].map(lambda x: level_order.get(x, 0))
log_sorted = log_pd.sort_values("timestamp")
if not log_sorted.empty:
    fig_timeline = px.line(
        log_sorted,
        x="timestamp",
        y="level_num",
        title="Log Levels Over Time",
        labels={"level_num": "level"},
    )
    fig_timeline.update_yaxes(tickvals=[0, 1, 2], ticktext=["INFO", "WARN", "ERROR"])
    fig_timeline.update_traces(mode="lines+markers")
    st.plotly_chart(fig_timeline)
else:
    st.info("No log timeline to display.")

# --- Anomalies: Error Count per Minute ---
stats_df = detect_anomaly(log_df, return_all=True)
anomaly_df = stats_df[stats_df["is_anomaly"]]

st.subheader("Anomalies detected in logs")
st.caption("Error Count per Minute")
if not stats_df.empty:
    fig_errors = px.line(
        stats_df,
        x="timestamp",
        y="error_count",
        title="Error Count per Minute",
    )
    fig_errors.update_traces(mode="lines+markers")
    st.plotly_chart(fig_errors)
else:
    st.info("No error counts to display.")

st.subheader("Anomalous Log Entries")
st.dataframe(anomaly_df)

if anomaly_df.empty:
    st.info("No anomalies detected with the current threshold.")

st.subheader("Email log report")
with st.expander("Send log summary and anomaly details by email"):
    report_email = st.text_input("Recipient email", value="ashigupta2616@gmail.com", placeholder="you@example.com", key="report_email")
    if st.button("Send log report"):
        if report_email and report_email.strip():
            try:
                send_log_report(report_email.strip(), stats_df, anomaly_df)
                st.success(f"Log report sent to {report_email}.")
            except Exception as e:
                st.error(f"Failed to send email: {e}")
        else:
            st.warning("Enter a recipient email address.")
