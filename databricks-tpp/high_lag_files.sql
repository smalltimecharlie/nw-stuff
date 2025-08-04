
SELECT *
FROM monitoring.cloud_file_ingestion
WHERE lag > INTERVAL 1 HOUR
ORDER BY lag DESC
LIMIT 10;
