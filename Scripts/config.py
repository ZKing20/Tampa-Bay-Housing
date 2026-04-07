import os
from datetime import datetime
# --- Directory Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, '..')

RAW_DIR = os.path.join(PROJECT_DIR, 'Data', 'Raw')
RAW_ZILLOW_DIR = os.path.join(RAW_DIR, 'Zillow')
RAW_CENSUS_DIR = os.path.join(RAW_DIR, 'Census')
RAW_CLEARINGHOUSE_DIR = os.path.join(RAW_DIR, 'Clearinghouse')

CLEANED_DIR = os.path.join(PROJECT_DIR, 'Data', 'Cleaned')
CLEAN_ZILLOW_DIR = os.path.join(CLEANED_DIR, 'Zillow')
CLEAN_CENSUS_DIR = os.path.join(CLEANED_DIR, 'Census')
CLEAN_CLEARINGHOUSE_DIR = os.path.join(CLEANED_DIR, 'Clearinghouse')

IMAGES_DIR = os.path.join(PROJECT_DIR, 'Images')

# --- Tampa Bay County Identifiers ---
# County names as they may appear in Zillow data
COUNTY_NAMES = [
    'Hillsborough County',
    'Pinellas County',
    'Pasco County',
    'Polk County',
]

# FIPS codes used by Census data to identify counties
COUNTY_FIPS = {
    'Hillsborough': '12057',
    'Pinellas': '12103',
    'Pasco': '12101',
    'Polk': '12105',
}

# State filter
STATE_FIPS = '12'  # Florida
STATE_NAME = 'Florida'

# --- Analysis Parameters ---
ANALYSIS_START_DATE = datetime(2014, 1, 1)
ANALYSIS_END_DATE = datetime(2024, 1, 1)

# Cost burden threshold (HUD standard)
COST_BURDEN_THRESHOLD = 30  # percent of income spent on housing
