import streamlit as st

from PIL import Image

st.set_page_config(
    page_title="A/B Testing App", page_icon=Image.open('img.png'), initial_sidebar_state="expanded"
)


st.write(
    """
# 📊 A/B Testing App
Upload your experiment results to see the significance of your A/B test.
"""
)