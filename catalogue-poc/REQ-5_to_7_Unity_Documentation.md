## 👤 REQ-5: Assign and Audit Dataset Ownership

**User Story**:  
> As a product owner, I need to assign and update dataset ownership.  
> Ownership fields are editable and auditable; changes are logged.

### ✅ Purpose
REQ-5 establishes clear ownership of datasets using the `owner` metadata property, ensuring accountability across data domains.

### 🔍 Implementation Highlights
- `owner` is added to each table using `ALTER TABLE SET TBLPROPERTIES`
- Ownership is visible through `SHOW TBLPROPERTIES`
- Ownership metadata changes are tracked through Databricks audit logs

### 💡 Governance Use Case
- Owners can be used to route DQ alerts or data queries
- Audits can filter ownership across catalog

### 🔗 Documentation
- [Unity Catalog Table Properties](https://docs.databricks.com/data-governance/unity-catalog/manage-privileges/table-properties.html)
- [Audit Logs in Unity Catalog](https://docs.databricks.com/administration-guide/account-settings/audit-logs.html)


## ✅ REQ-6: Display Permitted Use of Dataset

**User Story**:  
> As a user I need to understand permitted use of a dataset.  
> Permitted use is displayed clearly and tied to metadata or linked documents.

### ✅ Purpose
REQ-6 ensures users know what they’re allowed to do with a dataset (e.g. “internal use only”, “anonymised use”).

### 🔍 Implementation Highlights
- Added `permitted_use` field using `TBLPROPERTIES`
- Examples:
  - `internal only`
  - `analytics only`
  - `no marketing use`
- Allows downstream filtering, tool awareness, and responsible use

### 💡 Governance Use Case
- Displayed in data discovery platforms or notebooks
- Drives contextual warnings and dashboards

### 🔗 Documentation
- [Unity Catalog Table Properties](https://docs.databricks.com/data-governance/unity-catalog/manage-privileges/table-properties.html)


## ⛔ REQ-7: Reject Datasets Without Required Metadata

**User Story**:  
> As a platform admin, I need to reject datasets without required metadata.  
> Ingestion is blocked unless mandatory metadata fields are populated.

### ✅ Purpose
REQ-7 prevents unmanaged data from entering production by validating required metadata before usage or registration.

### 🔍 Implementation Highlights
- Simulated validation logic checks for:
  - `data_controller`
  - `data_processor`
  - `owner`
  - `retention_policy`
  - `permitted_use`
- Logic could be embedded in ingestion pipelines, governance checks, or APIs

### 💡 Governance Use Case
- Prevents ingestion of non-compliant datasets
- Supports “metadata contract” enforcement

### 🔗 Documentation
- [Unity Catalog Table Metadata](https://docs.databricks.com/data-governance/unity-catalog/manage-privileges/table-properties.html)
