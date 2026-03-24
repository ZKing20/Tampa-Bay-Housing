import os

# --- Directory Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, '..')

RAW_DIR = os.path.join(PROJECT_DIR, 'Data', 'Raw')
RAW_ZILLOW_DIR = os.path.join(RAW_DIR, 'Zillow')
RAW_CENSUS_DIR = os.path.join(RAW_DIR, 'Census')
RAW_CLEARINGHOUSE_DIR = os.path.join(RAW_DIR, 'Clearinghouse')

CLEANED_DIR = os.path.join(PROJECT_DIR, 'Data', 'Cleaned')
IMAGES_DIR = os.path.join(PROJECT_DIR, 'Images')

# --- Tampa Bay County Identifiers ---
# FIPS codes used by Census data to identify counties
TAMPA_BAY_COUNTIES = {
    'Hillsborough': '12057',
    'Pinellas': '12103',
    'Pasco': '12101',
    'Polk': '12105',
}

# County names as they may appear in Zillow data
COUNTY_NAMES = [
    'Hillsborough County',
    'Pinellas County',
    'Pasco County',
    'Polk County',
]

# State filter
STATE_FIPS = '12'  # Florida
STATE_NAME = 'Florida'

# --- Analysis Parameters ---
ANALYSIS_START_YEAR = 2014
ANALYSIS_END_YEAR = 2023

# Cost burden threshold (HUD standard)
COST_BURDEN_THRESHOLD = 30  # percent of income spent on housing
