# imports
import duckdb
import pandas as pd
import os
from config import CLEANED_DIR

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

        # TODO Register all tables

    return _CON
