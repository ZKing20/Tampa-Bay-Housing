# ---
# jupyter:
#   jupytext:
#     formats: py:percent,ipynb
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

"""
cleaning.py
-----------
Reads raw data from Data/Raw/, cleans and reshapes it,
and writes analysis-ready CSVs to Data/Cleaned/.

Run this script once before running any analysis or queries.
Re-run if raw data files are updated.

Data Sources:
    1. Zillow ZHVI & ZORI  (wide-format CSVs → long-format)
    2. Census ACS tables   (multi-file per year → merged single tables)
    3. FL Housing Data Clearinghouse (Excel workbooks → flat CSVs)
"""

# %%
# ============================================================
# Imports
# ============================================================
import pandas as pd
import numpy as np
import openpyxl
import os
import glob
from config import (
    RAW_ZILLOW_DIR, RAW_CENSUS_DIR, RAW_CLEARINGHOUSE_DIR,
    CLEANED_DIR, COUNTY_NAMES, COUNTY_FIPS,
    ANALYSIS_START_YEAR, ANALYSIS_END_YEAR
)

# %%
# ============================================================
# ZILLOW DATA CLEANING
# ============================================================

# Load ZHVI and ZORI CSVs
ZORI_County_Raw = pd.read_csv(os.path.join(RAW_ZILLOW_DIR, 'ZORI_County_Level_Raw.csv'))
ZORI_Metro_Raw = pd.read_csv(os.path.join(RAW_ZILLOW_DIR, 'ZORI_Metro_Level_Raw.csv'))
ZHVI_County_Raw = pd.read_csv(os.path.join(RAW_ZILLOW_DIR, 'ZHVI_County_Level_Raw.csv'))
ZHVI_Metro_Raw = pd.read_csv(os.path.join(RAW_ZILLOW_DIR, 'ZHVI_Metro_Level_Raw.csv'))

# Filter to Tampa Bay counties + national/metro rows
ZORI_County_Filtered = ZORI_County_Raw[(ZORI_County_Raw['StateName'] == 'FL') & 
                          (ZORI_County_Raw['RegionName'].isin(COUNTY_NAMES))]
ZORI_Metro_Filtered = ZORI_Metro_Raw[(ZORI_Metro_Raw['RegionName'].isin(['Tampa, FL', 'United States']))]
ZHVI_County_Filtered = ZHVI_County_Raw[(ZHVI_County_Raw['StateName'] == 'FL') & 
                          (ZHVI_County_Raw['RegionName'].isin(COUNTY_NAMES))]
ZHVI_Metro_Filtered = ZHVI_Metro_Raw[(ZHVI_Metro_Raw['RegionName'].isin(['Tampa, FL', 'United States']))]

# Unpivot from wide format (one column per month) to long format
ZORI_County_Long = pd.melt(ZORI_County_Filtered, id_vars = ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName', 'State', 'Metro', 'StateCodeFIPS', 'MunicipalCodeFIPS'], var_name = 'date', value_name = 'value')
ZORI_Metro_Long = pd.melt(ZORI_Metro_Filtered, id_vars = ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'], var_name = 'date', value_name = 'value')
ZHVI_County_Long = pd.melt(ZHVI_County_Filtered, id_vars = ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName', 'State', 'Metro', 'StateCodeFIPS', 'MunicipalCodeFIPS'], var_name = 'date', value_name = 'value')
ZHVI_Metro_Long = pd.melt(ZHVI_Metro_Filtered, id_vars = ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'], var_name = 'date', value_name = 'value')

# TODO: Save to Data/Cleaned/zillow_home_values.csv


# TODO: Save to Data/Cleaned/zillow_rents.csv


# %%
# ============================================================
# CENSUS ACS DATA CLEANING
# ============================================================

# Load B19013 files for each year (2014-2024)
raw_income_files = sorted(glob.glob(os.path.join(RAW_CENSUS_DIR, 'B19013_Median_Household_Income_Past_12_Months', '*.csv')))

# TODO: Clean and filter the raw data
clean_income_files = pd.concat(pd.melt(f, id_vars = [], var_name = '', value_name = 'median_income') for f in raw_income_files)

# Combine CSVs into one
Median_Household_Income = pd.concat((pd.read_csv(f) for f in clean_income_files), ignore_index=True)

# TODO: Save to Data/Cleaned/census_income.csv


# TODO: Load B25064 files (median gross rent) → census_rent.csv


# TODO: Load B25077 files (median home value) → census_home_value.csv


# TODO: Load B25070 files (rent as % of income) → census_rent_burden.csv


# %%
# ============================================================
# CLEARINGHOUSE DATA CLEANING
# ============================================================
# TODO: Load Excel workbooks for each county
# TODO: Read the 8 relevant sheets from each
# TODO: Combine into unified DataFrames
# TODO: Save to Data/Cleaned/clearinghouse.csv


# %%
# ============================================================
# VALIDATION
# ============================================================
# After cleaning, print summary stats to confirm data looks correct
def validate_cleaned_data():
    """Quick sanity checks on all cleaned files."""
    for filename in os.listdir(CLEANED_DIR):
        if filename.endswith('.csv'):
            filepath = os.path.join(CLEANED_DIR, filename)
            df = pd.read_csv(filepath)
            print(f"\n{'='*50}")
            print(f"{filename}")
            print(f"{'='*50}")
            print(f"  Shape: {df.shape}")
            print(f"  Columns: {list(df.columns)}")
            print(f"  Nulls:\n{df.isnull().sum().to_string()}")
            print(f"  First 3 rows:")
            print(df.head(3).to_string())


if __name__ == '__main__':
    # Run all cleaning steps, then validate
    # (Uncomment each section as you implement it)
    validate_cleaned_data()
