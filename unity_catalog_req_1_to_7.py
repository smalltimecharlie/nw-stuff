# Databricks Unity Catalog PoC – Requirements 1–7
# Author: ChatGPT
# Assumes Unity Catalog is enabled and configured in this workspace

from pyspark.sql import SparkSession

# Use a catalog/schema you have permissions on
catalog = "main"
schema = "uc_poc"
table_name = "req_test_dataset"

spark.sql(f"USE CATALOG {catalog}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {catalog}.{schema}")
spark.sql(f"USE SCHEMA {catalog}.{schema}")


# REQ-1: Register Metadata at Ingestion
# Metadata: data_controller, data_processor, retention_policy, owner

data = [
  ("Alice", "Engineering", 123),
  ("Bob", "Finance", 456)
]

columns = ["name", "department", "id"]
df = spark.createDataFrame(data, columns)

df.write.mode("overwrite").saveAsTable(f"{table_name}")

# Add metadata via table properties
spark.sql(f"""
ALTER TABLE {table_name}
SET TBLPROPERTIES (
  'data_controller' = 'DPO Team',
  'data_processor' = 'Data Platform',
  'retention_policy' = '1y',
  'owner' = 'data-owner@example.com'
)
""")

# REQ-2: Audit and Filter by Controller/Processor
# Note: We simulate audit by describing the table

spark.sql(f"DESCRIBE EXTENDED {table_name}").show(truncate=False)

# Optionally: use Spark catalog APIs to query properties
desc = spark.sql(f"SHOW TBLPROPERTIES {table_name}")
desc.filter(desc.key.isin("data_controller", "data_processor")).show()


# REQ-3: Enforce Retention Policy Logic (simulated)

# Simulate a check for expired datasets (not built-in in Unity)
# This would typically be implemented with scheduled jobs or Delta Live Tables
props = dict(spark.sql(f"SHOW TBLPROPERTIES {table_name}").collect())
retention = props.get("retention_policy", "none")

print("Retention policy found:", retention)

# Simulated logic
if retention == "1y":
    print("✅ Dataset has valid retention policy.")
else:
    print("❌ Missing or invalid retention.")


# REQ-4: Link Datasets to Sharing Agreements

# Add link to data agreement as table property
spark.sql(f"""
ALTER TABLE {table_name}
SET TBLPROPERTIES (
  'data_agreement_url' = 's3://my-legal-bucket/agreements/agreement-1234.pdf'
)
""")

spark.sql(f"SHOW TBLPROPERTIES {table_name}").filter("key = 'data_agreement_url'").show()


# REQ-5: Assign and Audit Ownership

# This is done via the GRANT/REVOKE commands or owner change
# Requires privileges

# To check current owner
owner = spark.sql(f"SHOW GRANT ON TABLE {table_name}")
owner.show()


# REQ-6: Display Permitted Use

# Store permitted use policy (e.g., internal-only, no PII) as metadata
spark.sql(f"""
ALTER TABLE {table_name}
SET TBLPROPERTIES (
  'permitted_use' = 'internal analytics only'
)
""")

spark.sql(f"SHOW TBLPROPERTIES {table_name}").filter("key = 'permitted_use'").show()


# REQ-7: Block Ingestion Without Required Metadata (Simulated)

# Unity does not enforce schema validation at ingest. You must implement logic in ingestion jobs.

required_fields = ["data_controller", "data_processor", "retention_policy", "owner"]

tbl_props = spark.sql(f"SHOW TBLPROPERTIES {table_name}").collect()
tbl_dict = {row['key']: row['value'] for row in tbl_props}

missing = [f for f in required_fields if f not in tbl_dict]

if missing:
    print(f"❌ Cannot ingest dataset: missing required metadata fields: {missing}")
else:
    print("✅ All required metadata fields are present.")
