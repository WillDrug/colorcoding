#legacy
from . import CMapInterface
from math import ceil, sqrt
from random import random
from PIL import Image

class SimpleGenerator2(CMapInterface):

    def __init__(self, **kwargs):
        pass

    def to_bitmap(self, input_bytes: bytearray) -> list:
        pixel_num = ceil(input_bytes.__len__() / 2)
        square_index = ceil(sqrt(pixel_num))
        output_map = list()

        waszero=False
        for i in range(square_index):
            row = list()
            for j in range(square_index):
                px = list()
                if waszero:
                    row.append((int(random()*256),int(random()*256),int(random()*256)))
                else:
                    for ch in range(3):
                        if waszero:
                            px.append(0)
                        else:
                            try:
                                px.append(input_bytes.pop())
                            except IndexError:
                                px.append(0)
                                waszero = True
                    row.append(tuple(px))
            output_map.append(row)
            if waszero:
                break
        return output_map#list(map(list, zip(*output_map)))

    def from_bitmap(self, input_bitmap: list) -> bytearray:
        #input_bitmap = list(map(list, zip(*input_bitmap)))
        output_array = bytearray()
        for row in input_bitmap:
            for px in row:
                for byte in px:
                    if byte == 0:
                        return output_array[::-1]
                    else:
                        output_array.append(byte)
        return output_array[::-1]

    def to_image(self, input_bitmap: list) -> Image:
        im = Image.new('RGB', (input_bitmap.__len__(), input_bitmap[0].__len__()))
        px = im.load()
        for i in range(im.size[0]):
            for j in range(im.size[1]):
                px[i, j] = input_bitmap[i][j]
        return im

    def from_image(self, input_image: Image) -> bytearray:
        px = input_image.load()
        bmp = list()
        for i in range(input_image.size[0]):
            row = list()
            for j in range(input_image.size[1]):
                row.append(px[i, j])
            bmp.append(row)
        return bmp


class SimpleGenerator1(CMapInterface):



    def __init__(self, mark0, mark1, mark2, **kwargs):
        self.mark_2 = mark2
        self.mark_1 = mark1
        self.mark_0 = mark0


    def to_bitmap(self, input_bytes: bytearray) -> list:
        pixel_num = ceil(input_bytes.__len__() / 2)
        square_index = ceil(sqrt(pixel_num))
        output_map = list()

        row = list()
        cnt = 0
        for i in range(ceil(pixel_num / square_index) * square_index + 1):
            if cnt == square_index:
                output_map.append(row)
                row = list()
                cnt = 0
            if input_bytes.__len__() >= 2:
                row.append((input_bytes.pop(), input_bytes.pop(), self.mark_2))
            elif input_bytes.__len__() == 1:
                row.append((input_bytes.pop(), int(random() * 256), self.mark_1))
            else:
                row.append((int(random() * 256), int(random() * 256), self.mark_0))
            cnt += 1

        return output_map

    def from_bitmap(self, input_bitmap: list) -> bytearray:
        output_array = bytearray()
        for row in input_bitmap:
            for px in row:
                if px[2] == self.mark_2:
                    output_array.append(px[0])
                    output_array.append(px[1])
                elif px[2] == self.mark_1:
                    output_array.append(px[0])
                elif px[2] == self.mark_0:
                    continue
                else:
                    print('Wrong encoding origin! Exiting')
                    exit()
        return output_array[::-1]

    def to_image(self, input_bitmap: list) -> Image:
        im = Image.new('RGB', (input_bitmap.__len__(), input_bitmap[0].__len__()))
        px = im.load()
        for i in range(im.size[0]):
            for j in range(im.size[1]):
                px[i, j] = input_bitmap[i][j]
        return im

    def from_image(self, input_image: Image) -> bytearray:
        px = input_image.load()
        bmp = list()
        for i in range(input_image.size[0]):
            row = list()
            for j in range(input_image.size[1]):
                row.append(px[i, j])
            bmp.append(row)
        return bmp
