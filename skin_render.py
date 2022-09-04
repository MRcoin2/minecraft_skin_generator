import asyncio
from io import BytesIO

import MinePI

from PIL import Image


async def render(image, vr=30, hr=30):
    im = await MinePI.render_3d_skin(skin_image=image, vr=-vr, hr=hr)
    out = Image.new(mode="RGBA", size=(250, 400), color=(0,0,0,0))
    out.paste(im,(int((250-im.size[0])/2),int((400-im.size[1])/2)))
    return out


def create_preview(skin):
    hr = 30
    preview = []
    for angle in range(72):
        preview.append(asyncio.run(render(skin, hr=hr)))
        hr -= 5
    gif_preview = BytesIO()
    preview[0].save(gif_preview, format='GIF', save_all=True, append_images=preview[1:], disposal=2, loop=0)
    return gif_preview
