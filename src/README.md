# Setup
1. python -m venv venv
2. pip install -r requirements.txt

# How to run
- arg1 Execute type
  - M Migrate
- arg2 Datasource file
- arg3 Target db
- arg4 csv path
- arg5 Report name

# Example

1. Migration Data
- Extract Devmountain XML Data
- Prepare Data
- Generate Devmountain CSV Data
- Load CSV Data to SQLite
python run.py M ../data-devclub-1.xml ../database/devclub2022.db ../csv ../reports/data-devclub-report.json

2. Query Data
- Query Employee Data by region
  - python run.py Q ../database/devclub2022.db region all
  - python run.py Q ../database/devclub2022.db region "Canada"
- Query Employee Data by department
  - python run.py Q ../database/devclub2022.db dept all
  - python run.py Q ../database/devclub2022.db dept "Flight Planning"
- Query Employee Data by nationality
  - python run.py Q ../database/devclub2022.db nationality all
  - python run.py Q ../database/devclub2022.db nationality "Germany"

# Visualize
Go to src/visualize.ipynb