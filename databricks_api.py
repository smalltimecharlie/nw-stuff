# Databricks DLT Pipeline Monitoring API Utilities
# Script to track pipeline runs, durations, status, and provide monitoring insights.

import requests
import pandas as pd
from datetime import datetime
from collections import Counter
from pyspark.sql import SparkSession

# ---------- CONFIG ----------
DATABRICKS_HOST = "https://<your-workspace>.cloud.databricks.com"
TOKEN = dbutils.secrets.get(scope="monitoring", key="dlt_token")
PIPELINE_ID = "<your-pipeline-id>"

HEADERS = {"Authorization": f"Bearer {TOKEN}"}
spark = SparkSession.getActiveSession()

# ---------- API HELPERS ----------
def get_pipeline_updates():
    url = f"{DATABRICKS_HOST}/api/2.0/pipelines/{PIPELINE_ID}/updates"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get("updates", [])

def get_pipeline_config():
    url = f"{DATABRICKS_HOST}/api/2.0/pipelines/{PIPELINE_ID}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_update_details(update_id):
    url = f"{DATABRICKS_HOST}/api/2.0/pipelines/{PIPELINE_ID}/updates/{update_id}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def trigger_pipeline(full_refresh=False):
    url = f"{DATABRICKS_HOST}/api/2.0/pipelines/{PIPELINE_ID}/updates"
    response = requests.post(url, headers=HEADERS, json={"full_refresh": full_refresh})
    response.raise_for_status()
    return response.json()

# ---------- METRIC COLLECTION ----------
updates = get_pipeline_updates()

# Run states summary
state_counts = Counter([u["state"] for u in updates])
print("Run state summary:", state_counts)

# Run durations
print("\nRun durations:")
for u in updates:
    started = datetime.fromtimestamp(u["creation_time"] / 1000)
    ended = datetime.fromtimestamp(u["last_update_time"] / 1000)
    duration = ended - started
    print(f"{u['update_id']} took {duration} ({u['state']})")

# Alert on failed runs
latest = updates[0]
if latest["state"] != "COMPLETED":
    print(f"\n🚨 Pipeline FAILED or not complete: {latest['state']} — Cause: {latest.get('cause', 'Unknown')}")

# Save updates to Delta
df = pd.DataFrame(updates)
spark_df = spark.createDataFrame(df)
spark_df.write.mode("overwrite").saveAsTable("monitoring.dlt_run_history")

# ---------- PIPELINE CONFIG SNAPSHOT ----------
config = get_pipeline_config()
print("\nPipeline configuration:")
print("Name:", config.get("name"))
print("Channel:", config.get("channel"))
print("Storage:", config.get("storage"))
print("Target schema:", config.get("target"))
print("Edition:", config.get("edition"))
print("Configured tables:", config.get("tables", []))
print("Clusters:", config.get("clusters", []))

# ---------- FILES WAITING TO BE PROCESSED? ----------
# Not directly available via API, but you can estimate by:
# - Comparing file modification timestamps in S3 vs. latest `cloud_files_state_hms()` ingestion
# - Setting up a separate listing job for S3 paths to count new files
# - Checking Autoloader logs in the event log or system.events

print("\nTo estimate files waiting to be processed:")
print("1. Query 'cloud_files_state_hms()' for latest ingested file timestamp")
print("2. Compare against source file system (S3) to find newer files")
print("3. Or look in the DLT event log for 'discoveredFiles' without 'processedFiles'")

print("\nDLT pipeline monitoring summary complete.")
