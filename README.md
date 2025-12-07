# Oil and Gas Data Analyst Project: Pipeline Integrity and Logistics Audit

## Project Overview
The goal is to build a **Predictive Maintenance System** for energy infrastructure. You will process raw IoT sensor data to predict pipeline failures and optimize logistics fleets.
By the end, you will have a working **Big Data Pipeline** that automatically flags high-risk equipment for repair *before* it breaks, and a **PowerBI Dashboard** that executives can use to monitor network health in real-time.

## Project Structure
- `data/`: Raw and processed data storage.
- `sql/`: SQL scripts for schema creation and auditing.
- `scripts/`: Python scripts for data ingestion.
- `notebooks/`: Jupyter notebooks for ETL and Analysis.

## Key Findings (Mocked)
- **Pipeline Integrity**: 2 segments identified as "Non-Compliant" due to overdue inspections (>90 days).
- **Logistics Efficiency**: Hypothesis testing confirms that the new "Route B" significantly reduces energy consumption (p-value < 0.05).
- **Risk Prediction**: Random Forest model achieved 85% accuracy in predicting pipeline failure based on sensor telemetry.

## Tools & Technologies
- **PostgreSQL**: Structured data storage for inspection logs and master data.
- **MongoDB**: NoSQL storage for high-volume, unstructured sensor and GPS data.
- **PySpark**: Big data processing for joining and aggregating large datasets.
- **Python (Pandas, Scikit-learn)**: Statistical analysis and machine learning.
- **R**: Advanced statistical hypothesis testing.

## Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.8+**: [Download](https://www.python.org/downloads/)
- **MongoDB Community Server**: [Download](https://www.mongodb.com/try/download/community) (Ensure it's running as a service)
- **PostgreSQL**: [Download](https://www.postgresql.org/download/)
- **R Project**: [Download](https://cran.r-project.org/) (For statistical analysis)
- **Java 8, 11, or 17**: Required for PySpark. (Java 17 is recommended for newer Spark versions)

## Setup Instructions
1. Create a virtual environment: `python -m venv venv`
2. Activate environment: `.\venv\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run ingestion script: `python scripts/02_data_ingestion.py`
5. Launch Jupyter: `jupyter notebook`

## Resuming Work (After Restart)
If you restart your computer, follow these steps to get back up and running:
1. Open your terminal (Command Prompt or PowerShell).
2. Navigate to the project folder:
   ```bash
   cd "C:\Users\Admin\Oil and Gas data analyst\oil_and_gas_data_analyst_project"
   ```
3. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```
4. Ensure MongoDB is running (if not set as an automatic service).
5. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
