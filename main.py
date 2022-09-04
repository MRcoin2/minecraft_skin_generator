import asyncio
from io import BytesIO

import streamlit as st

import skin_maker
import skin_render
from PIL import Image



st.set_page_config(
    page_title="Minecraft Skin App", page_icon=Image.open('icon.png'), initial_sidebar_state="expanded"
)

st.write(
    """
# Minecraft Skin From Image Generator
"""
)

async def preview_updater(test):
    angle = 0
    while True:
        angle += 1

        if angle > 71:
            angle = 0
        test.image(preview[angle])

        await asyncio.sleep(0.08)


image = st.file_uploader('Upload an image from which you want to generate a skin.', type=['png', 'jpg', 'jpeg'], accept_multiple_files=False)

col1, col2 = st.columns(2)

with col1:
    generate_preview = st.button('Preview')

with col2:
    if image is not None:
        if generate_preview:
            skin = skin_maker.make_skin(image)
            hr = 30
            preview = []
            for angle in range(72):
                preview.append(asyncio.run(skin_render.render(skin, hr=hr)))
                hr -= 5
            gif_preview = BytesIO()
            preview[0].save(gif_preview,format='GIF',save_all=True, append_images=preview[1:], disposal=2, loop=0)
            st.image(gif_preview)
            # test = st.image('preview.apng')
            # asyncio.run(preview_updater(test))
            generate_preview = not generate_preview
