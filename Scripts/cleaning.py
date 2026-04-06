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
import openpyxl as op
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
ZORI_County_Filtered = ZORI_County_Filtered.drop(columns='State')
ZORI_Metro_Filtered = ZORI_Metro_Raw[(ZORI_Metro_Raw['RegionName'].isin(['Tampa, FL', 'United States']))]
ZHVI_County_Filtered = ZHVI_County_Raw[(ZHVI_County_Raw['StateName'] == 'FL') & 
                          (ZHVI_County_Raw['RegionName'].isin(COUNTY_NAMES))]
ZHVI_County_Filtered = ZHVI_County_Filtered.drop(columns='State')
ZHVI_Metro_Filtered = ZHVI_Metro_Raw[(ZHVI_Metro_Raw['RegionName'].isin(['Tampa, FL', 'United States']))]

# Unpivot from wide format (one column per month) to long format
ZORI_County_Long = pd.melt(
    ZORI_County_Filtered,
    id_vars = ['RegionID', 'SizeRank', 'RegionName',
               'RegionType', 'StateName', 'Metro',
               'StateCodeFIPS', 'MunicipalCodeFIPS'],
               var_name = 'date',
               value_name = 'value')
ZORI_Metro_Long = pd.melt(
    ZORI_Metro_Filtered,
    id_vars = ['RegionID', 'SizeRank', 'RegionName',
               'RegionType', 'StateName'],
               var_name = 'date',
               value_name = 'value')
ZHVI_County_Long = pd.melt(
    ZHVI_County_Filtered,
    id_vars = ['RegionID', 'SizeRank', 'RegionName',
               'RegionType', 'StateName', 'Metro',
               'StateCodeFIPS', 'MunicipalCodeFIPS'],
               var_name = 'date',
               value_name = 'value')
ZHVI_Metro_Long = pd.melt(
    ZHVI_Metro_Filtered,
    id_vars = ['RegionID', 'SizeRank', 'RegionName',
               'RegionType', 'StateName'],
               var_name = 'date',
               value_name = 'value')

# TODO: Save to Data/Cleaned/zillow_home_values.csv


# TODO: Save to Data/Cleaned/zillow_rents.csv


# %%
# ============================================================
# CENSUS ACS DATA CLEANING
# ============================================================

# Helper function for 3 of the 4 tables from the Census 
def clean_census_table(filename):
    # Load files for each year
    raw_files = sorted(glob.glob(os.path.join(RAW_CENSUS_DIR, filename, '*.csv')))

    # Add a 'Year' Column
    yearly_files = []
    for f in raw_files:
        df = pd.read_csv(f)
        year = os.path.basename(f).split('_')[0]
        df['Year'] = year
        yearly_files.append(df)

    # Combine all years into one dataframe
    yearly_combined = pd.concat(
        yearly_files,
        ignore_index = True
    )

    # Clean and filter the raw data
    yearly_combined.columns = yearly_combined.columns.str.replace('!!', ' ')
    estimate_cols = yearly_combined.columns[yearly_combined.columns.str.endswith(" Estimate")]
    yearly_combined = yearly_combined[estimate_cols.tolist() + ['Year']]
    yearly_combined.columns = yearly_combined.columns.str.removesuffix(' Estimate')
    yearly_combined.columns = yearly_combined.columns.str.removesuffix(', Florida')

    # Reformat to long data
    yearly_combined_long = pd.melt(
        yearly_combined, 
        id_vars = 'Year',
        var_name = 'County',
        value_name = 'value')

    # Convert values from strings to integer
    yearly_combined_long['value'] = yearly_combined_long['value'].str.replace(',', '')
    yearly_combined_long['value'] = pd.to_numeric(yearly_combined_long['value'])

    return yearly_combined_long

# Apply the helper function
Median_Household_Income_Clean = clean_census_table('B19013_Median_Household_Income_Past_12_Months')
Median_Gross_Rent_Clean = clean_census_table('B25064_Median_Gross_Rent')
Median_Home_Value_Clean = clean_census_table('B25077_Median_Value_Owner_Occupied_Housing_Units')


# Load B25070 files (rent as % of income) → census_rent_burden.csv
# Load files for each year
raw_files = sorted(glob.glob(os.path.join(RAW_CENSUS_DIR, 'B25070_Gross_Rent_Percentage_of_Household_Income', '*.csv')))

# Add a 'Year' Column
yearly_files = []
for f in raw_files:
    df = pd.read_csv(f)
    year = os.path.basename(f).split('_')[0]
    df['Year'] = year
    yearly_files.append(df)

# Combine all years into one dataframe
yearly_combined = pd.concat(
    yearly_files,
    ignore_index = True
)

# Clean and filter the raw data
yearly_combined.columns = yearly_combined.columns.str.replace('!!', ' ')
estimate_cols = yearly_combined.columns[yearly_combined.columns.str.endswith((" Estimate", "(Grouping)"))]
yearly_combined = yearly_combined[estimate_cols.tolist() + ['Year']]
yearly_combined.columns = yearly_combined.columns.str.removesuffix(' Estimate')
yearly_combined.columns = yearly_combined.columns.str.removesuffix(', Florida')
yearly_combined.rename(columns={'Label (Grouping)': 'Bracket'}, inplace=True)
burden_category = {"Total": None, "Less than 10.0 percent": "not_burdened",
                   "10.0 to 14.9 percent": "not_burdened", "15.0 to 19.9 percent": "not_burdened",
                   "20.0 to 24.9 percent": "not_burdened", "25.0 to 29.9 percent": "not_burdened", 
                   "30.0 to 34.9 percent": "burdened", "35.0 to 39.9 percent": "burdened",
                   "40.0 to 49.9 percent": "burdened", "50.0 percent or more": "burdened",
                   "Not computed": "not_computed"}
yearly_combined['Bracket'] =  yearly_combined['Bracket'].str.strip().str.rstrip(':')
yearly_combined['burden_category'] = yearly_combined['Bracket'].map(burden_category)

# Reformat to long data
yearly_combined_long = pd.melt(
    yearly_combined,
    id_vars = ('Bracket', 'Year', 'burden_category'),
    var_name = 'County',
    value_name = 'value',
)

# Convert values from strings to integer
yearly_combined_long['value'] = yearly_combined_long['value'].str.replace(',', '')
yearly_combined_long['value'] = pd.to_numeric(yearly_combined_long['value'])

# TODO: Save to Data/Cleaned/census_income.csv


# %%
# ============================================================
# CLEARINGHOUSE DATA CLEANING
# ============================================================
# TODO: Load Excel workbooks for each county
def clean_clearinghouse_table(filename):
    raw_files = sorted(glob.glob(os.path.join(RAW_CLEARINGHOUSE_DIR, '*.xlsx')))
    homeownership_files = []
    for f in raw_files:
        df = pd.read_excel(f, sheet_name='Sheet 4', header=2)
        homeownership_files.append(df)

    # Combine into unified DataFrames
    homeownership_combined = pd.concat(homeownership_files, ignore_index=True)
    print(homeownership_combined)

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
