# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %%
# Imports and establish database connection
from db_connections import get_connection
con = get_connection()

# %%
# ============================================================
# QUESTION 1: How have home values and rents changed from
# 2014 to 2023, and how does Tampa Bay compare to the national average?
# ============================================================

# Home Value (Likely not needed)
def load_home_value_difference():

    # Define query
    query = f"""
        WITH starting_value AS (
            SELECT
                County,
                value AS starting_value
            FROM
                census_home_value_clean
            WHERE
                year = 2014
                ),
        ending_value AS (
            SELECT
                County,
                value AS ending_value
            FROM
                census_home_value_clean
            WHERE
                year = 2024
                )
        SELECT
            ev.ending_value - sv.starting_value AS home_value_dif,
            sv.County
        FROM
            starting_value sv
        JOIN
            ending_value ev ON sv.County = ev.County
        ORDER BY
            home_value_dif DESC
    """
    df = con.execute(query).fetchdf()
    return df

# Monthly Home prices
def load_monthly_home_value():
    query = f"""
        SELECT
            RegionName, date, value
        FROM
            ZHVI_clean
        ORDER BY 
            RegionName, date
    """
    df = con.execute(query).fetchdf()
    return df

# Monthly Rent prices
def load_monthly_rent_value():
    query = f"""
        SELECT
            RegionName, date, value
        FROM
            ZORI_clean
        ORDER BY 
            RegionName, date
    """
    df = con.execute(query).fetchdf()
    return df

# TODO: Percentage change in home values from 2014-2024 for each county vs Tampa metro vs national


# TODO: Percentage change in rent from 2014-2024 for each county vs Tampa metro vs national
 


# %%
# ============================================================
# QUESTION 2: Have household incomes kept pace with housing
# cost increases? What is the gap?
# ============================================================

# TODO: Percentage change in median income, median rent, and median home value from 2014 to 2024, by county and for the US


# TODO: Rent as a percentage of income for each county and year


# TODO: Home value as a multiple of income for each county and year


# %%
# ============================================================
# QUESTION 3: Which counties have experienced the most severe
# affordability squeeze?
# ============================================================

# TODO: Combined query that ranks the four counties by income growth vs rent growth vs home value growth


# TODO: Rent burden rates by county


# TODO: Homeownership rates by county


# %%
# ============================================================
# QUESTION 4: What percentage of renter households are
# cost-burdened, and how has that changed over the decade?
# ============================================================

# TODO: Total renters vs cost-burdened renters by county by year


# TODO: Breakdown by burden severity by county and year


# TODO: The change in cost-burdened percentage from 2014 to 2024 by county


# %%
# ============================================================
# QUESTION 5: How did COVID-19 specifically accelerate or
# change housing affordability trends?
# ============================================================

# TODO: Monthly home values and rents from ZHVI/ZORI, split into pre-COVID (2014–2019) and post-COVID (2020–2024)


# TODO: Year-over-year percentage change in home values and rents by month


# TODO: Income vs housing cost growth pre-COVID vs post-COVID
 

# %%
# Testing
if __name__ == '__main__':
    None
