import cv2
import numpy as np
from PIL import Image

img = Image.open('./img/apple.jpg')  # 画像読み込み
img = img.convert('RGB')
size = img.size

img_negaposi = Image.new('RGB',size)
for x in range(size[0]):
    #y
    for y in range(size[1]):
        #ピクセルを取得
        r,g,b = img.getpixel((x,y))

        #補色計算
        r = 255 - r
        g = 255 - g
        b = 255 - b

        #set pixel
        img_negaposi.putpixel((x,y),(r,g,b,0))

img_negaposi.save("./img/apple_negaposi.jpg")

img_hoshoku = Image.new('RGB',size)
for x in range(size[0]):
    #y
    for y in range(size[1]):
        #ピクセルを取得
        r,g,b = img.getpixel((x,y))

        #最大最小取得
        max_rgb = max(r,g,b)  #RGB最大
        min_rgb = min(r,g,b)  #RGB最小

        #補色計算
        r = (max_rgb+min_rgb)-r
        g = (max_rgb+min_rgb)-g
        b = (max_rgb+min_rgb)-b

        #set pixel
        img_hoshoku.putpixel((x,y),(r,g,b,0))

img_hoshoku.save("./img/apple_hoshoku.jpg")