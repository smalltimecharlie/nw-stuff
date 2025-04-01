# Databricks DLT Monitoring Setup Package
# Includes: DLT run tracking, cloud_files_state ingestion stats, dashboard SQL, and Teams alert integration

import requests
import pandas as pd
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

# ---------- CONFIG ----------
pipeline_id = "<YOUR_PIPELINE_ID>"
host = "https://<your-workspace>.cloud.databricks.com"
token = dbutils.secrets.get(scope="monitoring", key="dlt_token")
teams_webhook = dbutils.secrets.get(scope="monitoring", key="teams_webhook")

dashboard_table_run_history = "monitoring.dlt_run_history"
dashboard_table_file_ingestion = "monitoring.cloud_file_ingestion"
dashboard_catalog = "main"
dashboard_schema = "raw_data"
dashboard_table = "your_table"

headers = {"Authorization": f"Bearer {token}"}
spark = SparkSession.getActiveSession()

# ---------- DLT RUN TRACKING ----------
def collect_dlt_run_history():
    url = f"{host}/api/2.0/pipelines/{pipeline_id}/updates"
    response = requests.get(url, headers=headers).json()
    updates = response.get("updates", [])

    run_data = []
    for u in updates:
        run_data.append({
            "update_id": u["update_id"],
            "pipeline_id": u["pipeline_id"],
            "state": u["state"],
            "creator": u.get("creator_user_name"),
            "start_time": datetime.fromtimestamp(u["creation_time"] / 1000),
            "last_update_time": datetime.fromtimestamp(u["last_update_time"] / 1000),
            "cause": u.get("cause", "UNKNOWN")
        })

    df = spark.createDataFrame(pd.DataFrame(run_data))
    df.write.mode("overwrite").saveAsTable(dashboard_table_run_history)
    return run_data

# ---------- CLOUD FILE INGESTION TRACKING ----------
def collect_file_ingestion():
    query = f"""
    SELECT 
      current_timestamp() AS collected_at,
      path,
      size,
      modification_time,
      ingestion_timestamp,
      ingestion_timestamp - modification_time AS lag
    FROM cloud_files_state_hms('{dashboard_catalog}', '{dashboard_schema}', '{dashboard_table}')
    """
    df = spark.sql(query)
    df.write.mode("overwrite").saveAsTable(dashboard_table_file_ingestion)

# ---------- ALERTING ----------
def send_alert(message):
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": "DLT Monitoring Alert",
        "themeColor": "0076D7",
        "title": "DLT Pipeline Alert",
        "text": message
    }
    requests.post(teams_webhook, json=payload)

def alert_on_failed_runs(run_data):
    if not run_data:
        return
    last = run_data[0]
    if last["state"] != "COMPLETED":
        msg = f"🚨 DLT Pipeline *{pipeline_id}* failed or stuck!\nState: {last['state']}\nCause: {last['cause']}"
        send_alert(msg)

def alert_on_ingestion_lag():
    df = spark.sql(f"SELECT MAX(lag) as max_lag FROM {dashboard_table_file_ingestion}")
    max_lag = df.collect()[0]["max_lag"]
    if max_lag is not None and max_lag.total_seconds() > 3600:
        send_alert(f"⚠️ High ingestion lag detected: {max_lag}")

# ---------- MAIN ----------
run_data = collect_dlt_run_history()
collect_file_ingestion()
alert_on_failed_runs(run_data)
alert_on_ingestion_lag()
print("\nDLT monitoring job completed successfully.")
