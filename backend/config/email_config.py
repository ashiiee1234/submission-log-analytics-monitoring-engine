import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

# EMAIL="arushisharma0345@gmail.com"
# PASSWORD="xmnr atqo ejhm gapx"
# SMTP_SERVER="smtp.gmail.com"
# SMTP_PORT=465

# def send_mail(to_mail:str,anomaly:dict):
#     subject="Log anomaly detected"
#     body=f"""
#         Anomaly detected in system logs
#         time window: {anomaly['timestamp']}
#         Error count: {anomaly['error_count']}
#         Z score: {anomaly['z_score']}
#         Please review log data.

#         Regards,
#         Ashi Gupta.
# """
#     msg=EmailMessage()
#     msg["subject"]=subject
#     msg["from"]=EMAIL
#     msg["to"]=to_mail
#     msg.set_content(body)

#     with smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT) as server:
#         server.login(EMAIL,PASSWORD)
#         server.send_message(msg) 

import os

EMAIL = os.environ.get("LOG_EMAIL", "arushisharma0345@gmail.com")
PASSWORD = os.environ.get("LOG_EMAIL_PASSWORD", "xmnr atqo ejhm gapx")  # Set via env or replace with Gmail app password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465


def send_mail(to_mail: str, anomaly: dict):
    """Send a single anomaly alert email."""
    subject = "Log anomaly detected"
    body = f"""
        Anomaly detected in system logs
        time window: {anomaly['timestamp']}
        Error count: {anomaly['error_count']}
        Z score: {anomaly['z_score']}
        Please review log data.

        Regards,
        Ashi Gupta.
"""
    _send_email(to_mail, subject, body)


def send_log_report(to_mail: str, stats_df, anomaly_df):
    """
    Send an email with log analytics summary and anomaly details.
    stats_df: DataFrame with timestamp, error_count, z_score, is_anomaly (from detect_anomaly(..., return_all=True))
    anomaly_df: DataFrame of anomalous rows only (same columns).
    """
    total_minutes = len(stats_df) if stats_df is not None and not stats_df.empty else 0
    total_errors = int(stats_df["error_count"].sum()) if stats_df is not None and not stats_df.empty else 0
    num_anomalies = len(anomaly_df) if anomaly_df is not None and not anomaly_df.empty else 0

    lines = [
        "Log Analytics Report",
        "====================",
        "",
        f"Time windows (1 min): {total_minutes}",
        f"Total errors in period: {total_errors}",
        f"Anomalies detected: {num_anomalies}",
        "",
    ]
    if anomaly_df is not None and not anomaly_df.empty:
        lines.append("Anomalous windows (timestamp | error_count | z_score):")
        lines.append("-" * 50)
        for _, row in anomaly_df.iterrows():
            ts = row.get("timestamp", "")
            cnt = row.get("error_count", "")
            z = row.get("z_score", "")
            lines.append(f"  {ts}  |  {cnt}  |  {z}")
        lines.append("")
    lines.extend([
        "Please review log data and dashboard as needed.",
        "",
        "Regards,",
        "Ashi Gupta.",
    ])
    body = "\n".join(lines)
    subject = "Log Analytics Report" + (" – Anomalies Detected" if num_anomalies else " – Summary")
    _send_email(to_mail, subject, body)


def _send_email(to_mail: str, subject: str, body: str):
    msg = EmailMessage()
    msg["subject"] = subject
    msg["from"] = EMAIL
    msg["to"] = to_mail
    msg.set_content(body.strip())
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg) 