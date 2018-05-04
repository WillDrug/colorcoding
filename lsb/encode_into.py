from PIL import Image
from random import random
from numpy import unpackbits, packbits, ubyte, mean
from math import ceil


class NotAnImage(Exception):
    pass

class OutOfSpace(Exception):
    pass

class SimpleLSBEncoder:
    def __init__(self, input_image, encoding='utf-8'):
        self.encoding = encoding
        if isinstance(input_image, str):
            input_image = Image.open(input_image)
        if isinstance(input_image, Image.Image):
            self.im = input_image
            self.px = self.im.load()
        else:
            raise NotAnImage(f'Input image expected, {input_image.__class__} found')

    def encode(self, input_text: str) -> Image:
        input_bytes = bytearray(input_text.encode(self.encoding))
        input_bits = list()
        for q in input_bytes:
            for z in unpackbits(ubyte(q)):
                input_bits.append(z)
        if self.im.size[0]*self.im.size[1] < input_bits.__len__()+ceil(input_bits.__len__()/255):
            raise OutOfSpace('Image is not large enough for a bitwise encode')
        # encode LSB
        self.bitlength = input_bits.__len__()

        for i in range(self.im.size[0]):
            for j in range(self.im.size[1]):
                c1, c2, c3 = self.px[i, j]
                # encode here
                b = input_bits.pop()
                c1 = packbits(list(unpackbits(ubyte(c1))[:-3]) + [b, b, b])[0]
                c2 = packbits(list(unpackbits(ubyte(c2))[:-3]) + [b, b, b])[0]
                c3 = packbits(list(unpackbits(ubyte(c3))[:-3]) + [b, b, b])[0]
                self.px[i, j] = (c1,c2,c3)
                if input_bits.__len__() == 0:
                    break
            else:
                continue
            break
        return True

    def decode(self) -> str:
        output_bits = list()
        for i in range(self.im.size[0]):
            for j in range(self.im.size[1]):
                # outcode
                c1, c2, c3 = self.px[i, j]
                output_bits.append(
                    int(
                        round(
                            mean((
                                    round(
                                        mean(
                                            unpackbits(ubyte(c1))[-3:]
                                        )
                                    ),
                                    round(
                                        mean(
                                            unpackbits(ubyte(c2))[-3:]
                                        )
                                    ),
                                    round(
                                        mean(
                                            unpackbits(ubyte(c3))[-3:]
                                        )
                                    )
                                ))
                        )
                    )
                )
                if output_bits.__len__() == self.bitlength:
                    break
            else:
                continue
            break

        output_bits = output_bits[::-1]


        output_bytes = bytearray()
        byte = list()
        for b in output_bits:
            if byte.__len__() == 8:
                output_bytes.append(packbits(byte)[0])
                byte = list()
            byte.append(b)
        output_bytes.append(packbits(byte)[0])
        return output_bytes.decode(self.encoding)
