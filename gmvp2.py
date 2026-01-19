#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# Add a sidebar
st.sidebar.title("Navigate")
section = st.sidebar.radio("Go to", ["Introduction", "US Stock Market", "Volatility and Metrics", "Volatility Clustering", "GMVP Portfolio"])

# Introduction and Research Goal
if section == "Introduction":
    st.write("# Optimal Asset Allocation")
    # ... (rest of the introduction section)

# United States Stock Market in 2020
if section == "US Stock Market":
    st.write("# United State Stock Market in 2020")
    # ... (rest of the US Stock Market section)

# Volatility, Beta, and Value at Risk
if section == "Volatility and Metrics":
    st.write("# Volatility, Beta, and Value at Risk")
    # ... (rest of the Volatility and Metrics section)

    # Volatility Clustering Visualization
if section == "Volatility Clustering":
    st.write("# Volatility Clustering Visualization")
    # ... (rest of the Volatility Clustering section)

# Global Minimum Variance Portfolio
if section == "GMVP Portfolio":
    st.write("# The Global Minimum Variance Portfolio")
    # ... (rest of the GMVP Portfolio section)

# You can add more sections in a similar fashion

# Finally, add a Thank You section at the end
st.write("# Thank You")

