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

# %%
# Import packages
import os, sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Import eda_queries
try:
    current_file_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    current_file_dir = os.getcwd()

project_root = os.path.dirname(current_file_dir)

scripts_path = os.path.join(project_root, 'Scripts')

for path in [project_root, scripts_path]:
    if path not in sys.path:
        sys.path.append(path)

try:
    from eda_queries import *
except ModuleNotFoundError:
    print("Import failing. Current Search Paths:")
    for p in sys.path[-3:]: print(f"  - {p}")

# ── Color Palettes ──
county_palette = {
    'Hillsborough': '#1f77b4',   # Blue
    'Pinellas': '#ff7f0e',       # Orange
    'Pasco': '#2ca02c',          # Green
    'Polk': '#d62728',           # Red
}

# Images output directory
IMAGES_DIR = os.path.join(project_root, 'Images')

# %%
# ============================================================
# QUESTION 1 VISUALIZATIONS
# ============================================================

# TODO: Implement plots


# %%
# ============================================================
# QUESTION 2 VISUALIZATIONS
# ============================================================

# TODO: Implement plots


# %%
# ============================================================
# QUESTION 3 VISUALIZATIONS
# ============================================================

# TODO: Implement plots


# %%
# ============================================================
# QUESTION 4 VISUALIZATIONS
# ============================================================

# TODO: Implement plots


# %%
# ============================================================
# QUESTION 5 VISUALIZATIONS
# ============================================================

# TODO: Implement plots
