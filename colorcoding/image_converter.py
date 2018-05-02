from abc import ABCMeta, abstractmethod
from PIL import Image
# legacy
class ImageConverterInterface(metaclass=ABCMeta):
    @abstractmethod
    def to_image(self, input_data: list) -> Image:
        pass
    @abstractmethod
    def from_image(self, input_image: Image) -> list:
        pass


class StraightBMPConverter(ImageConverterInterface):
    def to_image(self, input_data: list, mode='RGB') -> Image:
        x = input_data.__len__()
        y = input_data[0].__len__()
        im = Image.new(mode, (x,y))
        pm = im.load()
        for i in range(x):
            for j in range(y):
                pm[i, j] = input_data[i][j]
        return im

    def from_image(self, input_image: Image) -> list:
        return_bmp = list()
        pm = input_image.load()
        for i in range(input_image.size[0]):
            row = list()
            for j in range(input_image.size[1]):
                row.append(pm[i, j])
            return_bmp.append(row)
        return return_bmp
