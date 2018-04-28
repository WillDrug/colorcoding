from PIL import Image
from math import ceil, sqrt
from random import random
import sys

mark_2 = 255
mark_1 = 100
mark_0 = 50

def generate_bitmap(input_string):
    input_bytes = bytearray(input_string.encode('utf-8'))

    pixel_num = ceil(input_bytes.__len__()/2)
    square_index = ceil(sqrt(pixel_num))
    output_map = list()

    row = list()
    cnt = 0
    for i in range(ceil(pixel_num/square_index)*square_index+1):
        if cnt == square_index:
            output_map.append(row)
            row = list()
            cnt = 0
        if input_bytes.__len__() >= 2:
            row.append((input_bytes.pop(), input_bytes.pop(), mark_2))
        elif input_bytes.__len__() == 1:
            row.append((input_bytes.pop(), int(random()*256), mark_1))
        else:
            row.append((int(random()*256), int(random()*256), mark_0))
        cnt += 1
    return output_map


def generate_image(bitmap):
    im = Image.new('RGB', (bitmap.__len__(), bitmap[0].__len__()))
    px = im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            px[i, j] = bitmap[i][j]
    return im