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
        - zillow_home_values  (monthly ZHVI by county/metro)
        - zillow_rents        (monthly ZORI by county/metro)
        - census_income       (median household income by county/year)
        - census_rent         (median gross rent by county/year)
        - census_home_value   (median home value by county/year)
        - census_rent_burden  (rent as % of income brackets by county/year)
        - fhdc_cost_burden    (cost burden by income level, from Clearinghouse)
        - fhdc_homeownership  (homeownership rate time series)
        - fhdc_affordable_units (affordable/available units per 100 renters)
    """
    global _CON

    if _CON is None:
        _CON = duckdb.connect()

        # --- Register each cleaned CSV as a table ---
        # Add registrations here as you complete each cleaning step.
        # Example:
        # _CON.register('zillow_home_values',
        #     pd.read_csv(os.path.join(CLEANED_DIR, 'zillow_home_values.csv')))

    return _CON
