#!/usr/bin/python
from PIL import Image
import os, sys

path = "C:/temp/FireDetection/FireNet/tmp/images/"
dirs = os.listdir( path )

for item in dirs:
    if '_d2n' not in item:
        continue
    if os.path.isfile(path+item):
        im_d2n = Image.open(path+item)
        f, e = os.path.splitext(path+item)
        im = Image.open(f[:-4]+e)
        # print(item)
        # break
        imResize = im_d2n.resize((im.size[0],im.size[1]), Image.ANTIALIAS)
        # imResize.save(f + '_resized.jpg', 'JPEG', quality=90)
        imResize.save(f+e, 'JPEG', quality=90)