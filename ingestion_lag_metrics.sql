
SELECT 
  MAX(lag) AS max_lag,
  AVG(lag) AS avg_lag
FROM monitoring.cloud_file_ingestion;
