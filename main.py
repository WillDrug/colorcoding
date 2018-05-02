import sys
from colorcoding.bitmap_encoder import SquareMapper
from colorcoding.image_converter import StraightBMPConverter

def neighbour_match(pixel_map, pxx, pxy):
    matched = 0
    color = pixel_map[pxx, pxy]
    for i in range(pxx-1, pxx+1):
        for j in range(pxy-1, pxy+1):
            try:
               if pixel_map[i, j] == color:
                   matched += 1
            except IndexError:
                pass
    return matched

from PIL import Image

import numpy
from matplotlib import pyplot

im = Image.open('compressed.jpg')
pxmap = im.load()
matches = list()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        matches.append(neighbour_match(pxmap, 0, 0))
print(matches.count(2))



"""f = open('test_vid.mp4', 'rb+')
input_data = bytearray(f.read())
f.close()

f = open('test_decoded.mp4', 'wb+')
for bt in dcd:
    f.write(bt)
f.close()
"""