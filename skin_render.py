import MinePI

async def render(image, vr=30, hr=30):
    im = await MinePI.render_3d_skin(skin_image=image, vr=-vr, hr=hr)
    return im