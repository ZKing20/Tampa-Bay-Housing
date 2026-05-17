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
            100 * ((ev.ending_value - sv.starting_value) / sv.starting_value) AS home_value_pct_change,
            sv.County
        FROM
            starting_value sv
        JOIN
            ending_value ev ON sv.County = ev.County
        ORDER BY
            home_value_pct_change DESC
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

# Percentage change in home values from 2014-2024 for each county vs Tampa metro vs national
def load_home_value_change():
    query = f"""
       SELECT
            RegionName,
            date,
            value,
            LAG(value) OVER(PARTITION BY RegionName ORDER BY date) AS previous_value,
            ((value - LAG(value) OVER(PARTITION BY RegionName ORDER BY date)) 
                / LAG(value) OVER(PARTITION BY RegionName ORDER BY date)) * 100 AS pct_change
        FROM
            ZHVI_clean
        ORDER BY
            RegionName, date
    """
    df = con.execute(query).fetchdf()
    return df

# Percentage change in rent from 2014-2024 for each county vs Tampa metro vs national
def load_rent_value_change():
    query = f"""
       SELECT
            RegionName,
            date,
            value,
            LAG(value) OVER(PARTITION BY RegionName ORDER BY date) AS previous_value,
            ((value - LAG(value) OVER(PARTITION BY RegionName ORDER BY date)) 
                / LAG(value) OVER(PARTITION BY RegionName ORDER BY date)) * 100 AS pct_change
        FROM
            ZORI_clean
        ORDER BY
            RegionName, date
    """
    df = con.execute(query).fetchdf()
    return df

# %%
# ============================================================
# QUESTION 2: Have household incomes kept pace with housing
# cost increases? What is the gap?
# ============================================================

# Percentage change in median income, median rent, and median home value from 2014 to 2024, by county and for the US
def load_median_pct_change():
    query = f"""
        WITH starting_home_value AS (
            SELECT
                County,
                value AS starting_home_value
            FROM
                census_home_value_clean
            WHERE
                year = '2014'
                ),
        ending_home_value AS (
            SELECT
                County,
                value AS ending_home_value
            FROM
                census_home_value_clean
            WHERE
                year = '2024'
                ),
        starting_rent_value AS (
            SELECT
                County,
                value AS starting_rent_value
            FROM
                census_rent_clean
            WHERE
                year = '2014'
                ),
        ending_rent_value AS (
            SELECT
                County,
                value AS ending_rent_value
            FROM
                census_rent_clean
            WHERE
                year = '2024'
                ),
        starting_income AS (
            SELECT
                County,
                value AS starting_income
            FROM
                census_income_clean
            WHERE
                year = '2014'
                ),
        ending_income AS (
            SELECT
                County,
                value AS ending_income
            FROM
                census_income_clean
            WHERE
                year = '2024'
                )
        SELECT
            100 * ((ehv.ending_home_value - shv.starting_home_value) / shv.starting_home_value) AS home_value_pct_change,
            100 * ((erv.ending_rent_value - srv.starting_rent_value) / srv.starting_rent_value) AS rent_value_pct_change,
            100 * ((ei.ending_income - si.starting_income) / si.starting_income) AS income_pct_change,
            shv.County
        FROM
            starting_home_value shv
        JOIN
           starting_rent_value srv ON shv.County = srv.County
        JOIN    
           starting_income si ON shv.County = si.County
        JOIN
            ending_home_value ehv ON shv.County = ehv.County
        JOIN
            ending_rent_value erv ON shv.County = erv.County
        JOIN    
            ending_income ei ON shv.County = ei.County
        ORDER BY
            home_value_pct_change DESC,
            rent_value_pct_change DESC
    """
    df = con.execute(query).fetchdf()
    return df

# Rent as a percentage of income for each county and year
def load_rent_income_pct():
    query = f"""
        SELECT
            cr.County,
            cr.Year,
            100 * (cr.value * 12 / ci.value) AS rent_pct
        FROM
            census_rent_clean cr
        JOIN
            census_income_clean ci ON cr.County = ci.County AND cr.Year = ci.Year
        ORDER BY
            cr.County, cr.Year
    """
    df = con.execute(query).fetchdf()
    return df

# Home value as a multiple of income for each county and year
def load_home_value_multiple_of_income():
    query = f"""
         SELECT
            ch.County,
            ch.Year,
            (ch.value / ci.value) AS home_value_multiple
        FROM
            census_home_value_clean ch
        JOIN
            census_income_clean ci ON ch.County = ci.County AND ch.Year = ci.Year
        ORDER BY
            ch.County, ch.Year
    """
    df = con.execute(query).fetchdf()
    return df

# %%
# ============================================================
# QUESTION 3: Which counties have experienced the most severe
# affordability squeeze?
# ============================================================

# TODO: Combined query that ranks the four counties by income growth vs rent growth vs home value growth
def load_county_rankings():
    query = f"""
        
    """
    df = con.execute(query).fetchdf()
    return df

# TODO: Rent burden rates by county
def load_rent_burden_rate():
    query = f"""
        
    """
    df = con.execute(query).fetchdf()
    return df

# TODO: Homeownership rates by county
def load_homeownership_rate():
    query = f"""
        
    """
    df = con.execute(query).fetchdf()
    return df

# %%
# ============================================================
# QUESTION 4: What percentage of renter households are
# cost-burdened, and how has that changed over the decade?
# ============================================================

# TODO: Total renters vs cost-burdened renters by county by year
def load_cost_burdened_vs_total_renters():
    query = f"""
        
    """
    df = con.execute(query).fetchdf()
    return df

# TODO: Breakdown by burden severity by county and year
def load_burden_severity():
    query = f"""
        
    """
    df = con.execute(query).fetchdf()
    return df

# TODO: The change in cost-burdened percentage from 2014 to 2024 by county
def load_cost_burden_change():
    query = f"""
        
    """
    df = con.execute(query).fetchdf()
    return df

# %%
# ============================================================
# QUESTION 5: How did COVID-19 specifically accelerate or
# change housing affordability trends?
# ============================================================

# TODO: Monthly home values and rents from ZHVI/ZORI, split into pre-COVID (2014–2019) and post-COVID (2020–2024)
def load_pre_vs_post_covid_home_values():
    query = f"""
        
    """
    df = con.execute(query).fetchdf()
    return df

# TODO: Year-over-year percentage change in home values and rents by month
def load_yearly_rent_and_home_value_change():
    query = f"""
        
    """
    df = con.execute(query).fetchdf()
    return df

# TODO: Income vs housing cost growth pre-COVID vs post-COVID
def load_pre_vs_post_covid_income_vs_housing_cost():
    query = f"""
        
    """
    df = con.execute(query).fetchdf()
    return df

# %%
# Testing
if __name__ == '__main__':
    None
