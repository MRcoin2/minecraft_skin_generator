import asyncio
from io import BytesIO

import streamlit as st

import skin_maker
import skin_render
from PIL import Image

from bokeh.models.widgets import Div
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app






st.set_page_config(
    page_title="Minecraft Skin App", page_icon=Image.open('icon.png'), initial_sidebar_state="expanded"
)

st.write(
    """
# Minecraft Skin From Image Generator
"""
)

with st.expander("How to use.", expanded= True):
    st.write("""
             The chart above shows some numbers I picked for you.
             I rolled actual dice for these, so they're *guaranteed* to
             be random.
         """)
    st.image("https://static.streamlit.io/examples/dice.jpg")



image = st.file_uploader('Upload an image from which you want to generate a skin.', type=['png', 'jpg', 'jpeg'], accept_multiple_files=False)

col1, col2 = st.columns(2)
skin = None
with col1:
    st.write()
    generate_preview = st.button('Generate And Preview', disabled=image is None)

with col2:
    if image is not None:
        if generate_preview:
            skin = skin_maker.make_skin(image)
            preview_gif = skin_render.create_preview(skin)
            st.image(preview_gif)
            # test = st.image('preview.apng')
            # asyncio.run(preview_updater(test))
            generate_preview = not generate_preview
col3, col4, col5 = st.columns([1,1,4])
with col3:
    if skin is not None:
        output_skin = BytesIO()
        skin.save(output_skin,format='PNG')
        downloaded = st.download_button('Download', file_name='skin.png', data=output_skin)
    else:
        st.button('Download', disabled=True)
with col4:
    if st.button('Donate ❤',key='balls'):
        # st.markdown('<meta http-equiv="refresh" content="0;url=https://donate.stripe.com/test_4gw3cqcdCfoEa9W9AA">',unsafe_allow_html=True)
        js = "window.open('https://donate.stripe.com/test_4gw3cqcdCfoEa9W9AA')"  # New tab or window
        # js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
