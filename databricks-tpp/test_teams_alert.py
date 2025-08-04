
import requests

teams_webhook = "<YOUR_WEBHOOK_URL>"

def send_teams_alert(message):
    payload = {
        "@type": "MessageCard",
        "@context": "http://schema.org/extensions",
        "summary": "Test Message",
        "themeColor": "0076D7",
        "title": "Test Alert",
        "text": message
    }
    requests.post(teams_webhook, json=payload)

# Example query result
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
spark_result = spark.sql("SELECT COUNT(*) AS total FROM monitoring.dlt_run_history").collect()[0]["total"]
send_teams_alert(f"Test Alert: There are {spark_result} pipeline runs in the history table.")
