import MinePI
import asyncio
from PIL import Image, ImageTk

async def render(image, vr=30, hr=30):
    #Render a full body skin
    im = await MinePI.render_3d_skin(skin_image=image, vr=-vr, hr=hr)#, vrll=10, vrrl=-10, vrla=-10, vrra=10
    #
    # im.show()
    # im = ImageTk.getimage(im)
    return im
# asyncio.run(render())