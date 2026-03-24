# Tampa Bay Housing Affordability Analysis (2014–2023)

## Objective
Analyze how housing costs have outpaced household incomes in the Tampa Bay metro area over the past decade, using publicly available data from Zillow, the U.S. Census Bureau, and the Florida Housing Data Clearinghouse.

## Tools Used
- Python (Pandas, NumPy, Matplotlib, Seaborn, OpenPyXL)
- SQL via DuckDB (CTEs, Window Functions, Joins, Aggregations)
- Jupyter Notebook (via Jupytext)
- Tableau Public (interactive dashboard)

## Data Sources
All data sourced directly from primary government and research sources:
- **Zillow Research** (zillow.com/research/data): ZHVI (home values) and ZORI (rents), monthly time series
- **U.S. Census Bureau** (data.census.gov): American Community Survey 1-Year Estimates — Tables B19013, B25064, B25077, B25070
- **Florida Housing Data Clearinghouse** (flhousingdata.shimberg.ufl.edu): Cost burden, affordability metrics, homeownership rates

## Key Questions
1. **How have home values and rents in the Tampa Bay metro changed from 2014 to 2023, and how does that growth compare to the national average?**
2. **Have household incomes in the region kept pace with housing cost increases? What is the gap?**
3. **Which counties within the Tampa Bay metro have experienced the most severe affordability squeeze?**
4. **What percentage of renter households are now cost-burdened, and how has that changed over the decade?**
5. **How did COVID-19 specifically accelerate or change housing affordability trends?**

## Results
*Coming soon — analysis in progress.*

## Repository Structure
```
Tampa-Bay-Housing/
├── Data/
│   ├── Raw/                    Raw data files as downloaded (unmodified)
│   │   ├── Zillow/             ZHVI and ZORI CSVs
│   │   ├── Census/             ACS tables (B19013, B25064, B25077, B25070)
│   │   └── Clearinghouse/      Excel workbooks from FL Housing Data Clearinghouse
│   └── Cleaned/                Processed, analysis-ready CSVs
├── Scripts/
│   ├── config.py               Paths, constants, and county definitions
│   ├── cleaning.py             Data cleaning and reshaping logic
│   ├── db_connections.py       DuckDB setup — registers cleaned tables
│   └── eda_queries.py          All SQL queries organized by business question
├── Notebooks/
│   └── eda_visualizations.py   Plotting and visualization (Jupytext)
├── Images/                     Output charts organized by question
├── .vscode/                    Shared VS Code settings
├── .gitattributes              Line ending normalization (LF)
├── .gitignore                  Keeps large/unnecessary files out of repo
├── requirements.txt            Python dependencies
├── README.md                   This file
└── LICENSE                     MIT License
```

## Setup
```bash
# Clone the repo
git clone https://github.com/ZKing20/Tampa-Bay-Housing.git
cd Tampa-Bay-Housing

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
# .venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Run data cleaning (creates files in Data/Cleaned/)
cd Scripts
python cleaning.py

# Open notebooks
cd ../Notebooks
jupyter notebook
```
