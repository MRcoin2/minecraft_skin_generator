import streamlit as st

from PIL import Image

st.set_page_config(
    page_title="A/B Testing App", page_icon=Image.open('icon.png'), initial_sidebar_state="expanded"
)


st.write(
    """
# Minecraft Skin From Image Generator
Upload your image to generate a skin.
"""
)