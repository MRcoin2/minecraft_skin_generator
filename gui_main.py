import asyncio
import os

import PIL

import skin_maker
import skin_render
import PySimpleGUI as sg
from PIL import Image, ImageTk

sg.theme('DarkGray11')
display = sg.Frame('Preview',[[sg.Column([[sg.Image(key = '-DISPLAY-')]], justification='c', pad=0)]],size=(300,420))
input = sg.Frame('Input',[[sg.Column([[sg.Text('Image'),sg.Input('',size=(30,1), key='-IMAGE_PATH-'), sg.FileBrowse(target='-IMAGE_PATH-', size=(8,1))]], pad=0)]],expand_x=True)
output = sg.Frame('Output',[[sg.Column([[sg.Text('Image'),sg.Input('',size=(30,1), key='-SAVE_PATH-'), sg.SaveAs(target='-SAVE_PATH-', file_types=(('Skin file','*.png'),), size=(8,1))]], pad=0)]],expand_x=True)
layout = [[input],[output], [sg.Column([[sg.Button('Preview',expand_x=True,expand_y=True)],[sg.Button('Save',expand_x=True,expand_y=True)]],expand_y=True, pad=0),display]]

window = sg.Window('',layout,finalize=True, icon=b'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')

def make_skin(values):
    return skin

angle = 0
hr = 30
skin = None

while True:
    event, values = window.read(timeout=75)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == 'Preview':
        try:
            skin = skin_maker.make_skin(values['-IMAGE_PATH-'])
            hr = 30
            preview = []
            for angle in range(72):
                preview.append(asyncio.run(skin_render.render(skin, hr=hr)))
                hr -= 5

        except Exception:
            sg.PopupOK('Invalid image file')

    if event == 'Save':
        try:
            if skin == None:
                skin_maker.make_skin(values['-IMAGE_PATH-']).save(values['-SAVE_PATH-'])
                sg.PopupOK('Done')
            else:
                skin.save(values['-SAVE_PATH-'])
                sg.PopupOK('Done')
        except PIL.UnidentifiedImageError:
            sg.PopupOK('Invalid image file')

    if skin != None:
        window['-DISPLAY-'].update(
            data=ImageTk.PhotoImage(image=preview[angle]))
        angle += 1
        if angle > 71:
            angle = 0


window.close()
os.system('exit')

# zcacheować perspektywy skina do podglądu