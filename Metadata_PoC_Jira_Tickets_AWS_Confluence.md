# Metadata Catalogue PoC – Jira Ticket Breakdown (AWS Focused)

## Setup – Unity Catalog (Databricks on AWS)
**Story Points**: 3
**Description**:
Enable Unity Catalog in a Databricks workspace running on AWS. Link to S3 buckets and configure the metastore using AWS Glue. Create sample Delta tables and configure workspace audit logging. Assign test roles for ownership and access control.

## Setup – OpenMetadata on AWS (S3/Glue)
**Story Points**: 5
**Description**:
Deploy OpenMetadata in an AWS-native environment using EC2 or EKS. Configure ingestion pipelines for AWS Glue tables and S3 sources. Define test metadata schema including controller, processor, retention policy, and owner fields using custom properties or glossary tags.

## Setup – DataHub on AWS (Glue/Redshift)
**Story Points**: 5
**Description**:
Deploy DataHub using Docker or Kubernetes in AWS. Ingest metadata from AWS Glue and optionally Redshift. Test entity lineage and glossary term ingestion using the AWS plugins. Configure test ingestion pipelines and metadata schema validation.

## Unity Catalog – REQ-1
**Story Points**: 3
**Requirement**: Metadata registration at ingestion (controller, processor, retention, owner)
**Description**:
Evaluate **Unity Catalog** support for **metadata registration at ingestion (controller, processor, retention, owner)** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## Unity Catalog – REQ-2
**Story Points**: 3
**Requirement**: Audit/filter by controller/processor
**Description**:
Evaluate **Unity Catalog** support for **audit/filter by controller/processor** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## Unity Catalog – REQ-3
**Story Points**: 5
**Requirement**: Enforce retention policies with alert/flag
**Description**:
Evaluate **Unity Catalog** support for **enforce retention policies with alert/flag** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## Unity Catalog – REQ-4
**Story Points**: 3
**Requirement**: Link datasets to sharing agreements
**Description**:
Evaluate **Unity Catalog** support for **link datasets to sharing agreements** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## Unity Catalog – REQ-5
**Story Points**: 2
**Requirement**: Assign and audit ownership
**Description**:
Evaluate **Unity Catalog** support for **assign and audit ownership** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## Unity Catalog – REQ-6
**Story Points**: 2
**Requirement**: Display permitted use
**Description**:
Evaluate **Unity Catalog** support for **display permitted use** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## Unity Catalog – REQ-7
**Story Points**: 4
**Requirement**: Block ingestion without mandatory metadata
**Description**:
Evaluate **Unity Catalog** support for **block ingestion without mandatory metadata** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## OpenMetadata – REQ-1
**Story Points**: 3
**Requirement**: Metadata registration at ingestion (controller, processor, retention, owner)
**Description**:
Evaluate **OpenMetadata** support for **metadata registration at ingestion (controller, processor, retention, owner)** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## OpenMetadata – REQ-2
**Story Points**: 3
**Requirement**: Audit/filter by controller/processor
**Description**:
Evaluate **OpenMetadata** support for **audit/filter by controller/processor** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## OpenMetadata – REQ-3
**Story Points**: 5
**Requirement**: Enforce retention policies with alert/flag
**Description**:
Evaluate **OpenMetadata** support for **enforce retention policies with alert/flag** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## OpenMetadata – REQ-4
**Story Points**: 3
**Requirement**: Link datasets to sharing agreements
**Description**:
Evaluate **OpenMetadata** support for **link datasets to sharing agreements** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## OpenMetadata – REQ-5
**Story Points**: 2
**Requirement**: Assign and audit ownership
**Description**:
Evaluate **OpenMetadata** support for **assign and audit ownership** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## OpenMetadata – REQ-6
**Story Points**: 2
**Requirement**: Display permitted use
**Description**:
Evaluate **OpenMetadata** support for **display permitted use** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## OpenMetadata – REQ-7
**Story Points**: 4
**Requirement**: Block ingestion without mandatory metadata
**Description**:
Evaluate **OpenMetadata** support for **block ingestion without mandatory metadata** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## DataHub – REQ-1
**Story Points**: 3
**Requirement**: Metadata registration at ingestion (controller, processor, retention, owner)
**Description**:
Evaluate **DataHub** support for **metadata registration at ingestion (controller, processor, retention, owner)** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## DataHub – REQ-2
**Story Points**: 3
**Requirement**: Audit/filter by controller/processor
**Description**:
Evaluate **DataHub** support for **audit/filter by controller/processor** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## DataHub – REQ-3
**Story Points**: 5
**Requirement**: Enforce retention policies with alert/flag
**Description**:
Evaluate **DataHub** support for **enforce retention policies with alert/flag** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## DataHub – REQ-4
**Story Points**: 3
**Requirement**: Link datasets to sharing agreements
**Description**:
Evaluate **DataHub** support for **link datasets to sharing agreements** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## DataHub – REQ-5
**Story Points**: 2
**Requirement**: Assign and audit ownership
**Description**:
Evaluate **DataHub** support for **assign and audit ownership** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## DataHub – REQ-6
**Story Points**: 2
**Requirement**: Display permitted use
**Description**:
Evaluate **DataHub** support for **display permitted use** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.

## DataHub – REQ-7
**Story Points**: 4
**Requirement**: Block ingestion without mandatory metadata
**Description**:
Evaluate **DataHub** support for **block ingestion without mandatory metadata** in an **AWS-native setup** using S3, Glue, and IAM where applicable. Test ingestion of datasets stored in Amazon S3, with schemas defined in AWS Glue. Document whether the metadata fields can be captured natively at ingestion or modeled through tags, policies, or glossary extensions. Confirm that metadata is visible in the UI, searchable, filterable, auditable, and enforced where applicable.
