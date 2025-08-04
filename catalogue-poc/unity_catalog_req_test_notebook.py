# Databricks Unity Catalog – REQ-1 to REQ-7 Test Suite
# Catalog: `charlie_poc`, Schema: `governance_demo`, Table: `req_test_dataset`

# 🧱 Setup: Create Catalog and Schema (if not already created)
spark.sql("CREATE CATALOG IF NOT EXISTS charlie_poc")
spark.sql("USE CATALOG charlie_poc")
spark.sql("CREATE SCHEMA IF NOT EXISTS governance_demo")
spark.sql("USE SCHEMA governance_demo")


# COMMAND ----------

# 📦 REQ-1: Register Metadata at Ingestion

data = [("Alice", "Engineering", 123), ("Bob", "Finance", 456)]
columns = ["name", "department", "id"]
df = spark.createDataFrame(data, columns)

df.write.mode("overwrite").saveAsTable("charlie_poc.governance_demo.req_test_dataset")

spark.sql("""
ALTER TABLE charlie_poc.governance_demo.req_test_dataset
SET TBLPROPERTIES (
  'data_controller' = 'DPO Team',
  'data_processor' = 'Data Platform',
  'retention_policy' = '1y',
  'owner' = 'data-owner@example.com'
)
""")


# COMMAND ----------

# 🔍 REQ-2: Audit and Filter by Controller/Processor
spark.sql("SHOW TBLPROPERTIES charlie_poc.governance_demo.req_test_dataset") \
      .filter("key IN ('data_controller', 'data_processor')") \
      .show()


# COMMAND ----------

# ⏳ REQ-3: Enforce Retention Policy (Simulated)
tbl_props = dict(spark.sql("SHOW TBLPROPERTIES charlie_poc.governance_demo.req_test_dataset").rdd.map(lambda row: (row.key, row.value)).collect())
retention = tbl_props.get("retention_policy", "none")

print("Retention Policy:", retention)

if retention == "1y":
    print("✅ Retention policy is valid.")
else:
    print("❌ Retention policy missing or invalid.")


# COMMAND ----------

# 📄 REQ-4: Link Datasets to Sharing Agreements
spark.sql("""
ALTER TABLE charlie_poc.governance_demo.req_test_dataset
SET TBLPROPERTIES (
  'data_agreement_url' = 's3://my-legal-bucket/agreements/agreement-1234.pdf'
)
""")
spark.sql("SHOW TBLPROPERTIES charlie_poc.governance_demo.req_test_dataset") \
      .filter("key = 'data_agreement_url'") \
      .show()


# COMMAND ----------

# 👤 REQ-5: Assign and Audit Ownership
spark.sql("SHOW GRANT ON TABLE charlie_poc.governance_demo.req_test_dataset").show()


# COMMAND ----------

# 🔐 REQ-6: Display Permitted Use
spark.sql("""
ALTER TABLE charlie_poc.governance_demo.req_test_dataset
SET TBLPROPERTIES (
  'permitted_use' = 'internal analytics only'
)
""")
spark.sql("SHOW TBLPROPERTIES charlie_poc.governance_demo.req_test_dataset") \
      .filter("key = 'permitted_use'") \
      .show()


# COMMAND ----------

# 🚫 REQ-7: Block Ingestion Without Metadata (Simulated Check)
required_fields = ['data_controller', 'data_processor', 'retention_policy', 'owner']
tbl_props = dict(spark.sql("SHOW TBLPROPERTIES charlie_poc.governance_demo.req_test_dataset").rdd.map(lambda row: (row.key, row.value)).collect())
missing = [key for key in required_fields if key not in tbl_props]

if missing:
    print("❌ Missing required metadata fields:", missing)
else:
    print("✅ All required metadata fields are present.")
