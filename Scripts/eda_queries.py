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

# TODO: Home Value
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
            ev.ending_value - sv.starting_value AS home_value_dif
            County
        FROM
            starting_value sv
        JOIN
            ending_value ev ON sv.County = ev.County
        ORDER BY
            home_value_dif DESC
    """
    df = con.execute(query).fetchdf()
    return df

# TODO: Rent



# %%
# ============================================================
# QUESTION 2: Have household incomes kept pace with housing
# cost increases? What is the gap?
# ============================================================

# TODO: Implement queries


# %%
# ============================================================
# QUESTION 3: Which counties have experienced the most severe
# affordability squeeze?
# ============================================================

# TODO: Implement queries


# %%
# ============================================================
# QUESTION 4: What percentage of renter households are
# cost-burdened, and how has that changed over the decade?
# ============================================================

# TODO: Implement queries


# %%
# ============================================================
# QUESTION 5: How did COVID-19 specifically accelerate or
# change housing affordability trends?
# ============================================================

# TODO: Implement queries


# %%
# Testing
if __name__ == '__main__':
    None
