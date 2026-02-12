
# 🚀 Execution Commands
Run these commands in order to start the project:

* **Generate Logs**: python log_generation/log_generator.py

* **Process Data**: python main.py

* **Launch Dashboard**: streamlit run dashboard/app.py  `python run_dask_dashboard.py`

___

## 🚀 Log Analytics Engine
Software applications generate a continuous stream of logs that provide insight into how a system is running. These logs allow engineers to track system health, identify unusual behavior, troubleshoot issues, and understand performance over time. Turning this raw log data into meaningful information is an important part of maintaining reliable systems.

This project demonstrates a simple end-to-end logging pipeline that mimics a real-world workflow. It simulates realistic log data, processes and organizes it into a structured format, and presents the results through an interactive dashboard. The aim is to show how logs can be collected, transformed, and visualized in a clear and modular way.

___

## 🛠️ Features
* Real-time Ingestion & Parsing: Collects and normalizes system logs from distributed sources using Python logging and Regex for high-fidelity data extraction.

* Distributed Processing Pipeline: Leverages Dask and Ray frameworks for parallel log analysis, ensuring the engine can handle high-throughput, large-scale system data.

* Anomaly Detection Core: Implements statistical models, including Z-score calculations, to identify unusual behavior and potential system failures in real-time.

* Alerting & Notification Hub: Integrated system for triggering automated alerts via Email (SMTP) or Webhooks when critical anomalies are detected.

* Interactive Analytics Dashboard: A comprehensive Streamlit interface for visualizing log trends, pie charts of system activity, and anomaly tracking.

* Agile Project Management: Development tracked through structured sprints, user stories, and MoSCoW prioritization, documented in the included **AGILE TEMPLATE**.

* Interactive dashboard built with Streamlit for visualization

* Modular and extensible design for easy customization and scaling

---

