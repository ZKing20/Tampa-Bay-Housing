# imports
import duckdb
import pandas as pd
from config import CLEAN_ZILLOW_DIR, CLEAN_CLEARINGHOUSE_DIR, CLEAN_CENSUS_DIR

# Global Connection Holder
_CON = None

def get_connection():
    """
    Returns a DuckDB connection with all cleaned datasets
    registered as queryable tables. Uses a singleton pattern
    so the connection is only created once.

    Tables registered:
        - ZHVI_clean                         (monthly ZHVI by county/metro)
        - ZORI_clean                         (monthly ZORI by county/metro)
        - census_income_clean                (median household income by county/year)
        - census_rent_clean                  (median gross rent by county/year)
        - census_home_value_clean            (median home value by county/year)
        - census_rent_burden_clean           (rent as % of income brackets by county/year)
        - clearinghouse_homeownership_clean  (homeownership rate time series)
    """
    global _CON

    if _CON is None:
        # Initialiize DuckDB connection
        _CON = duckdb.connect()

        # Register all tables
        tables = {
            'ZHVI_clean': f'{CLEAN_ZILLOW_DIR}/ZHVI_clean.csv',
            'ZORI_clean': f'{CLEAN_ZILLOW_DIR}/ZORI_clean.csv',
            'census_income_clean': f'{CLEAN_CENSUS_DIR}/census_income_clean.csv',
            'census_rent_clean': f'{CLEAN_CENSUS_DIR}/census_rent_clean.csv',
            'census_home_value_clean': f'{CLEAN_CENSUS_DIR}/census_home_value_clean.csv',
            'census_rent_burden_clean': f'{CLEAN_CENSUS_DIR}/census_rent_burden_clean.csv',
            'clearinghouse_homeownership_clean': f'{CLEAN_CLEARINGHOUSE_DIR}/clearinghouse_homeownership_clean.csv',
                }

        for table_name, filepath in tables.items():
            _CON.register(table_name, pd.read_csv(filepath))

    return _CON
