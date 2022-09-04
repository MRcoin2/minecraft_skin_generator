import MinePI

from PIL import Image


async def render(image, vr=30, hr=30):
    im = await MinePI.render_3d_skin(skin_image=image, vr=-vr, hr=hr)
    out = Image.new(mode="RGBA", size=(250, 400), color=(0,0,0,0))
    out.paste(im,(int((250-im.size[0])/2),int((400-im.size[1])/2)))
    return out