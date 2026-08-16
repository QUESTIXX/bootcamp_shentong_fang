# NYU Student Health Center Data Cleaning & Predictive Readiness Pipeline
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
The NYU Student Health Center (SHC) collects diverse student health records, including routine clinical visits, triage logs, and mental health screening surveys. However, raw health data is severely siloed, noisy, inconsistent (e.g., varying coding standards, high rate of missing values), and contains protected health information (PHI). 

This data quality bottleneck prevents clinical researchers and campus public health analysts from reliably training early-warning predictive models (e.g., predicting seasonal flu spikes, high-risk mental health escalations, or chronic disease management needs). This project aims to build an automated, privacy-preserving data cleaning and standardization pipeline to transform raw clinical logs into analysis-ready feature stores, drastically reducing data preparation time and unlocking predictive capabilities for campus health monitoring.

## Stakeholder & User
- **Primary Stakeholders (Decision Makers):** 
  - *Director of NYU Student Health Center & Chief Medical Officer*: Needs aggregated epidemiological insights and data integrity assurance to allocate medical staff and plan wellness interventions.
- **End Users (Operators & Consumers):** 
  - *Healthcare Data Scientists / Biostatisticians*: Directly consume the cleaned dataset and feature pipelines to train risk prediction models.
  - *Clinical Research Coordinators*: Use the standardized data dictionaries to query cohort statistics.
- **Workflow Context & Timing:** 
  - Processed data must be updated on a bi-weekly cadence to support real-time campus health trend dashboards and semester-long predictive modeling research.

## Useful Answer & Decision
- **Type of Framing:** 
  - *Descriptive & Diagnostic* (Data profiling reports, missingness patterns, patient cohort summary).
  - *Predictive-Enabling* (Structured feature store ready for classification algorithms like Logistic Regression/XGBoost for disease risk).
- **Key Metrics & Deliverables:**
  - *Data Quality Metrics:* Missing data rate (<5% in critical clinical features), Schema validation pass rate (100%), Duplicate record reduction rate.
  - *Artifacts to Deliver:* 
    1. Automated data preprocessing & cleaning scripts (`src/clean_pipeline.py`).
    2. Comprehensive Data Dictionary and Quality Profiling Report (`docs/data_dictionary.md`).
    3. Standardized, de-identified clean tabular dataset (`data/processed/`).

## Assumptions & Constraints
- **HIPAA / FERPA Compliance & Privacy:** All raw identifiers (Student ID, Name, Phone) must be irreversibly hashed or removed (De-identification) before downstream modeling.
- **Data Availability:** Initial scope assumes access to structured CSV/JSON clinical logs and survey data; unstructured clinical free-text notes are excluded from Stage 01.
- **Data Quality Assumption:** Missingness in vital signs is assumed to be Missing at Random (MAR) or Missing Completely at Random (MCAR), allowing for statistical imputation.
- **Compute Constraints:** The pipeline must run locally or on standard cloud environments without requiring distributed high-performance computing clusters.

## Known Unknowns / Risks
- **Measurement Bias / Data Drift:** Survey formats and check-in question codes may change across academic semesters.
- **Imputation Risk:** Aggressive imputation on clinical vitals could introduce artificial correlation.
- **Monitoring & Mitigation:** Implement automated unit tests and schema assertion checks (e.g., using `pytest` or `Great Expectations`) before data enters the modeling stage.

## Lifecycle Mapping
Goal → Stage → Deliverable
- **Establish Data Framing & Repo Structure** → Problem Framing & Scoping (Stage 01) → *Project Scoping README & Stakeholder Memo*
- **Data Audit & Exploratory Analysis** → Exploratory Data Analysis (Stage 02) → *EDA Notebook & Missingness Profiling Report*
- **Build Preprocessing & Feature Pipeline** → Feature Engineering & Pipeline (Stage 03) → *Python ETL Scripts & Clean Dataset*
- **Baseline Risk Prediction Modeling** → Model Development (Stage 04) → *Baseline Predictive Model & Evaluation Report*

## Repo Plan
- `data/`: Contains raw sample data (`raw/`) and processed, de-identified datasets (`processed/`). (Note: raw sensitive data is ignored in `.gitignore`).
- `src/`: Core Python modules for data cleaning, type validation, and feature generation.
- `notebooks/`: Exploratory Data Analysis (EDA) and experimental cleaning prototypes.
- `docs/`: Data dictionary, Stakeholder Memo, schema contracts, and milestone reports.
- **Update Cadence:** Weekly sync with sprint branch merges into `main` after passing automated data validation tests.