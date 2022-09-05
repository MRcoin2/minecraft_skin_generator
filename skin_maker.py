import base64
import io
import random

from PIL import Image
from colorthief import ColorThief


def make_skin(path, custom_fill_color):
    img = Image.open(path).convert("RGBA")
    # img.show()
    # img = img.convert("RGBA")
    img = img.resize((24, 36), Image.ANTIALIAS)
    # img.show()

    face_and_sides = img.crop((0, 4, 24, 12))

    head_top = img.crop((8, 0, 16, 4))
    head_bot_fill = img.crop((8, 11, 16, 12))

    torso_top_fill = img.crop((8, 12, 16, 13))
    torso_r_fill = img.crop((8, 12, 9, 24))
    torso = img.crop((8, 12, 16, 24))
    torso_l_fill = img.crop((16, 12, 17, 24))
    torso_bot_fill = img.crop((8, 24, 16, 25))

    r_arm_top = img.crop((4, 8, 8, 12))
    r_arm = img.crop((4, 12, 8, 24))
    r_arm_side = img.crop((0, 12, 4, 24))
    r_arm_bot = img.crop((4, 24, 8, 28))
    r_arm_fill = img.crop((7, 12, 8, 24))

    l_arm_top = img.crop((16, 8, 20, 12))
    l_arm = img.crop((16, 12, 20, 24))
    l_arm_side = img.crop((20, 12, 24, 24))
    l_arm_bot = img.crop((16, 24, 20, 28))
    l_arm_fill = img.crop((16, 12, 17, 24))

    r_leg_top_fill = img.crop((8, 24, 12, 25))
    r_leg_fill = img.crop((12, 24, 13, 36))
    r_leg = img.crop((8, 24, 12, 36))
    r_leg_side = img.crop((4, 24, 8, 36))

    l_leg_top_fill = img.crop((12, 24, 16, 25))
    l_leg_fill = img.crop((12, 24, 13, 36))
    l_leg = img.crop((12, 24, 16, 36))
    l_leg_side = img.crop((16, 24, 20, 36))
    # skin = Image.open("mask.png").convert("RGBA")
    skin = Image.open(io.BytesIO(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKqWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4gPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNi4wLWMwMDYgNzkuZGFiYWNiYiwgMjAyMS8wNC8xNC0wMDozOTo0NCAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCBDQyAoV2luZG93cykiIHhtcDpDcmVhdGVEYXRlPSIyMDIxLTA0LTA5VDEyOjUxOjU2KzAyOjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAyMS0xMi0zMVQwMToyMzoyMSswMTowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAyMS0xMi0zMVQwMToyMzoyMSswMTowMCIgZGM6Zm9ybWF0PSJpbWFnZS9wbmciIHBob3Rvc2hvcDpDb2xvck1vZGU9IjMiIHBob3Rvc2hvcDpJQ0NQcm9maWxlPSJzUkdCIElFQzYxOTY2LTIuMSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo4ZGIwZjU2OC1hMjQ2LTIwNGMtODAzYy1jNjJhMmE4NmNkNGEiIHhtcE1NOkRvY3VtZW50SUQ9ImFkb2JlOmRvY2lkOnBob3Rvc2hvcDowMjY1MTViMy01ODEzLTA3NDQtOTdkYS00ZTI0NTc3YzgzMzkiIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo4MDM4NTY0MS1iMzRjLWY3NDItOTdjMi1jNGQ2MjViYjFmY2UiPiA8eG1wTU06SGlzdG9yeT4gPHJkZjpTZXE+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJjcmVhdGVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOjgwMzg1NjQxLWIzNGMtZjc0Mi05N2MyLWM0ZDYyNWJiMWZjZSIgc3RFdnQ6d2hlbj0iMjAyMS0wNC0wOVQxMjo1MTo1NiswMjowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0iY29udmVydGVkIiBzdEV2dDpwYXJhbWV0ZXJzPSJmcm9tIGltYWdlL3BuZyB0byBhcHBsaWNhdGlvbi92bmQuYWRvYmUucGhvdG9zaG9wIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo0MzMzOTYxYS0zZDFmLTdiNDUtYTk5Mi05OTQ1MDE1ZTExMDAiIHN0RXZ0OndoZW49IjIwMjEtMDQtMDlUMTM6MDc6MTUrMDI6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDQyAoV2luZG93cykiIHN0RXZ0OmNoYW5nZWQ9Ii8iLz4gPHJkZjpsaSBzdEV2dDphY3Rpb249InNhdmVkIiBzdEV2dDppbnN0YW5jZUlEPSJ4bXAuaWlkOmZjM2RkYzZjLTU3OWMtNWE0NC1hNjJiLWI2YzcwNzcwYmY4NSIgc3RFdnQ6d2hlbj0iMjAyMS0wNC0wOVQxMzowNzoyNyswMjowMCIgc3RFdnQ6c29mdHdhcmVBZ2VudD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0iY29udmVydGVkIiBzdEV2dDpwYXJhbWV0ZXJzPSJmcm9tIGFwcGxpY2F0aW9uL3ZuZC5hZG9iZS5waG90b3Nob3AgdG8gaW1hZ2UvcG5nIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJkZXJpdmVkIiBzdEV2dDpwYXJhbWV0ZXJzPSJjb252ZXJ0ZWQgZnJvbSBhcHBsaWNhdGlvbi92bmQuYWRvYmUucGhvdG9zaG9wIHRvIGltYWdlL3BuZyIvPiA8cmRmOmxpIHN0RXZ0OmFjdGlvbj0ic2F2ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6M2M4NDMxMTUtOTFjYy03ODRkLTgyMTMtYmM3YWIzYmMwMDdkIiBzdEV2dDp3aGVuPSIyMDIxLTA0LTA5VDEzOjA3OjI3KzAyOjAwIiBzdEV2dDpzb2Z0d2FyZUFnZW50PSJBZG9iZSBQaG90b3Nob3AgQ0MgKFdpbmRvd3MpIiBzdEV2dDpjaGFuZ2VkPSIvIi8+IDxyZGY6bGkgc3RFdnQ6YWN0aW9uPSJzYXZlZCIgc3RFdnQ6aW5zdGFuY2VJRD0ieG1wLmlpZDo4ZGIwZjU2OC1hMjQ2LTIwNGMtODAzYy1jNjJhMmE4NmNkNGEiIHN0RXZ0OndoZW49IjIwMjEtMTItMzFUMDE6MjM6MjErMDE6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCAyMi40IChXaW5kb3dzKSIgc3RFdnQ6Y2hhbmdlZD0iLyIvPiA8L3JkZjpTZXE+IDwveG1wTU06SGlzdG9yeT4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6ZmMzZGRjNmMtNTc5Yy01YTQ0LWE2MmItYjZjNzA3NzBiZjg1IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjgwMzg1NjQxLWIzNGMtZjc0Mi05N2MyLWM0ZDYyNWJiMWZjZSIgc3RSZWY6b3JpZ2luYWxEb2N1bWVudElEPSJ4bXAuZGlkOjgwMzg1NjQxLWIzNGMtZjc0Mi05N2MyLWM0ZDYyNWJiMWZjZSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Prcv610AAADrSURBVHic7drRDoIwEAXRYvr/v1zf1YBkwWOyd56xTCabFgnbOGZ9cc0eW/H3Jdba13/8yONvSQAtoEkALaBJAC2gmaN+zh9xtD59Tmg/AQmgBTQJoAU0CaAFNHO8n8PVc/vsc8Xr9dX1Tz1XtJ+ABNACmm3c/1+Astba3RPaT0ACaAFNAmgBTQJoAU0CaAFNAmgBzaf3Aa1oPwEJoAU0CaAFNAmgBTQJoAU0CaAFNAmgBTQJoAU084Y17/6+4NL3F+0nIAG0gOaKPaD6TVD1fqU9of0EJIAW0CSAFtAkgBbQJIAW0CSAFtA8AX//E4EsaOBrAAAAAElFTkSuQmCC'))).convert("RGBA")
    # skin = Image.new('RGBA', (64, 64))
    # skin.putalpha(255)
    color_thief = ColorThief(path)
    # color0, color1 = color_finder.color_check()
    if custom_fill_color is not None:
        color0 = tuple(int(custom_fill_color.strip('#')[i:i+2], 16) for i in (0, 2, 4))
    else:
        color0 = color_thief.get_color()
    # r0,g0,b0 = color0[0]
    # r1,g1,b1 = color1[0]
    r0, g0, b0 = color0
    # r1,g1,b1 = color1
    for w in range(skin.size[0]):
        for h in range(skin.size[1]):
            r, g, b, a = skin.getpixel((w, h))
            if a == 255:
                lum_shift = random.randint(-10, 10)
                skin.putpixel((w, h), (r0 + lum_shift, g0 + lum_shift, b0 + lum_shift, 255))
                # print("0")

    # skin.paste((200,200,200), [0,0,skin.size[0],skin.size[1]])

    skin.paste(face_and_sides, (0, 8), face_and_sides)
    skin.paste(head_top, (8, 4), head_top)
    for i in range(8):
        skin.paste(head_bot_fill, (16, i), head_bot_fill)

    for i in range(4):
        skin.paste(torso_r_fill, (i + 16, 20), torso_r_fill)
    for i in range(4):
        skin.paste(torso_top_fill, (20, i + 16), torso_top_fill)
    skin.paste(torso, (20, 20), torso)
    for i in range(4):
        skin.paste(torso_bot_fill, (28, i + 16), torso_bot_fill)
    for i in range(4):
        skin.paste(torso_l_fill, (i + 28, 20), torso_l_fill)

    skin.paste(r_arm_top, (44, 16), r_arm_top)
    skin.paste(r_arm, (44, 20), r_arm)
    skin.paste(r_arm_side, (40, 20), r_arm_side)
    skin.paste(r_arm_bot, (48, 16), r_arm_bot)
    for i in range(4):
        skin.paste(r_arm_fill, (i + 48, 20), r_arm_fill)

    skin.paste(l_arm_top, (36, 48), l_arm_top)
    skin.paste(l_arm, (36, 52), l_arm)
    skin.paste(l_arm_side, (40, 52), l_arm_side)
    skin.paste(l_arm_bot, (40, 48), l_arm_bot)
    for i in range(4):
        skin.paste(l_arm_fill, (i + 32, 52), l_arm_fill)

    for i in range(4):
        skin.paste(r_leg_top_fill, (4, i + 16), r_leg_top_fill)
    skin.paste(r_leg, (4, 20), r_leg)
    skin.paste(r_leg_side, (0, 20), r_leg_side)
    for i in range(4):
        skin.paste(r_leg_fill, (i + 8, 20), r_leg_fill)

    for i in range(4):
        skin.paste(l_leg_top_fill, (20, i + 48), l_leg_top_fill)
    skin.paste(l_leg, (20, 52), l_leg)
    skin.paste(l_leg_side, (24, 52), l_leg_side)
    for i in range(4):
        skin.paste(l_leg_fill, (i + 16, 52), l_leg_fill)
    return skin
# skin.save(f"out{time.time()}.png")