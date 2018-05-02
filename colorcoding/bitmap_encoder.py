from math import ceil, sqrt
from random import random
from abc import ABCMeta, abstractmethod
# legacy
class BitmapConverterInterface(metaclass=ABCMeta):
    @abstractmethod
    def to_bmp(self, input_data):
        pass
    @abstractmethod
    def from_bmp(self, input_data):
        pass


class SquareMapper(BitmapConverterInterface):
    def to_bmp(self, input_data: bytearray) -> list:
        input_data = input_data[::-1]
        si = int(sqrt(input_data.__len__()))
        waszero = False
        output_map = list()
        for i in range(si):
            row = list()
            for j in range(si):
                if waszero:
                    row.append((int(random()*256),int(random()*256),int(random()*256)))
                else:
                    px = list()
                    for q in range(3):
                        try:
                            px.append(input_data.pop())
                        except IndexError:
                            waszero = True
                            px.append(0)
                row.append(tuple(px))
            output_map.append(row)
        return output_map

    def from_bmp(self, input_data: list) -> bytearray:
        output_data = bytearray()
        for i in input_data:
            for j in i:
                for q in j:
                    if q == 0:
                        return output_data
                    else:
                        output_data.append(q)
        return output_data

