import asyncio
from io import BytesIO

import streamlit as st
from streamlit_cropper import st_cropper

import skin_maker
import skin_render
from PIL import Image

from bokeh.models.widgets import Div

# embed streamlit docs in a streamlit app






st.set_page_config(
    page_title="Minecraft Skin App", page_icon=Image.open('icon.png'), initial_sidebar_state="expanded"
)

st.write(
    """
# Minecraft Skin From Image Generator
"""
)

with st.expander("How to use.", expanded= False):
    st.write("""
             Here are some tips on how to get the best results with this tool:
         """)

    "⚪ Use properly cropped images."
    "The images you upload will be resized to fit the skin, to avoid stretching crop your images."
    st.image(Image.open('help1.png'))

    "⚪ Try using transparency."
    "If you want better effects try cutting your images out and using transparent PNGs."
    st.image(Image.open('help2.png'))
    "⚪ Adjust the fill color."
    "There is also an option for you to specify the fill color in case you don't like the auto-generated one."
    st.image(Image.open('help3.png'))


def box_algo(image, aspect_ratio):
    return {'left':0,'top':0,'width':image.size[0], 'height':image.size[1]}

image = st.file_uploader('Upload an image from which you want to generate a skin.', type=['png', 'jpg', 'jpeg', 'jfif'], accept_multiple_files=False)


# img = Image.open(image)
# coll, colr = st.columns(2)
# if image is not None:
#     with colr:
#         croping = st.button('Crop image')
#         if croping:
#             cropped_image = st_cropper(img, realtime_update=True, box_color='#FF4B4B',
#                                      aspect_ratio=None, box_algorithm=box_algo)
#     with coll:
#         st.write("Preview")
#         if croping:
#             _ = cropped_image.thumbnail((300, 300))
#             st.image(cropped_image)
#         else:
#             _ = img.thumbnail((300, 300))
#             st.image(img)


col1, col2 = st.columns(2)
skin = None
custom_fill_color = None
preview_gif = None
with col1:
    if st.checkbox('Choose custom fill color'):
        custom_fill_color = st.color_picker('Pick a fill color')
    generate_preview = st.button('Generate And Preview', disabled=image is None)

with col2:
    if generate_preview or preview_gif is not None:
        skin = skin_maker.make_skin(image, custom_fill_color)
        preview_gif = skin_render.create_preview(skin)
        st.image(preview_gif)
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
        js = "window.open('https://buy.stripe.com/4gw3etdt63yN5QkeUU')"  # New tab or window
        # js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)
