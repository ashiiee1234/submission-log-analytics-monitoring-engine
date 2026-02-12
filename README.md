# Log_Analytics_Monitoring_Engine
Python based high throughput log analytics monitoring engine

## Execution Commands

Run these commands in order to start the project:

1. **Generate Logs:** `python log_generation/log_generator.py`  
   (Starts real-time log producer; stop with Ctrl+C. Creates `realtime_logs.csv` in project root.)

2. **Process Data:** `python main.py`  
   (Starts the FastAPI backend on http://127.0.0.1:8000 for the frontend and API.)

3. **Launch Dashboard:** `streamlit run dashboard/app.py`  
   (Opens the log analytics dashboard in the browser.)
   `python run_dask_dashboard.py`
