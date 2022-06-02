from random import choice, randint;
from PIL import Image, ImageDraw;
import pyautogui as pg;
import os;
from time import sleep;


def imagegen(msg):
    lst=list("0123456789abcdef")
    width=height = 100
    color=lambda: ''.join([choice(lst),choice(lst),choice(lst)]).upper()
    textColor=lambda: randint(0,255)
    for i in range(10):
        img = Image.new('RGB', (width, height), color=f'#{color()}')
        imgDraw = ImageDraw.Draw(img)
        textWidth, textHeight = imgDraw.textsize(msg)
        xText = (width - textWidth) / 2
        yText = (height - textHeight) / 2
        imgDraw.text((xText, yText), msg, fill=(textColor(),textColor(),textColor()))
        img.save(f'img{i}.png')
        os.system(f"xclip -selection clipboard -t image/png -i img{i}.png")
        pg.hotkey("ctrl", "v")
    pg.press("enter")
n=int(input("Enter number of times to send 10 images: "))
msg=input("Enter message to send: ")
sleep(5)
for i in range(n):
    imagegen(msg)
    sleep(1.5)