import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats
from scipy.stats import norm
import altair as alt

st.set_page_config(
    page_title="A/B Testing App", page_icon="📊", initial_sidebar_state="expanded"
)


st.write(
    """
# 📊 A/B Testing App
Upload your experiment results to see the significance of your A/B test.
"""
)