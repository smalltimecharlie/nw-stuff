
SELECT date_trunc('hour', ingestion_timestamp) AS hour, COUNT(*) AS file_count
FROM monitoring.cloud_file_ingestion
GROUP BY hour
ORDER BY hour DESC;
