# from config.dask_config import start_dask
# from ingestion.loader import load_logs
# from ingestion.parser import parse_log_line
# from processing.pipeline import build_pipeline
# import time
# import dask.dataframe as df
# from anomaly.detecter import detect_anomaly
# from config.email_config import send_mail
from fastapi import FastAPI
from backend.router import service
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins=[     #Need to add origin so that frontend can send method to backend.
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, ## Allow connection to database.
    allow_methods=["*"], ##allow all methods like POST,GET,PUT,DELETD,etc.
    allow_headers=["*"],
)


# user_mail = "rohanbelsare113@gmail.com"
# def main():
    # client = start_dask()
    # print(client)
    # print(f"Dashboard link: {client.dashboard_link}")
    # print("\n" + "=" * 50)

    # start = time.time()
    # log_df = build_pipeline(r"data\sample_log.log")
    # print(log_df.tail())
    # print("start time:", start)

    # total_logs = log_df.count().compute()
    # end = time.time()

    # print("Running Anomaly detection...")
    # anomalies_df = detect_anomaly(log_df)

    # # anomalies = anomalies_df.compute()
    # anomalies = anomalies_df

    # if anomalies.empty:
    #     print("No anomalies detected")
    # else:
    #     print(f"🚨 {len(anomalies)} anomalies detected!")

    #     for _, row in anomalies.iterrows():
    #         anomaly_data = {
    #             "timestamp": row["timestamp"],
    #             "error_count": row["error_count"],
    #             "z_score": row["z_score"],
    #         }

    #         send_mail(to_email=user_mail, anomaly=anomaly_data)

    #         print(
    #             f"📧 Alert sent | Time: {row['timestamp']} | "
    #             f"Errors: {row['error_count']}"
    #         )

    # input("\nPress Enter to exit...")

app.include_router(service.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)


