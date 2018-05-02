










#legacy
from PIL import Image
from abc import ABCMeta, abstractmethod

class CMapInterface(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    def to_bitmap(self, input_bytes: bytearray) -> list:
        pass

    @abstractmethod
    def from_bitmap(self, input_bitmap: list) -> bytearray:
        pass

    @abstractmethod
    def to_image(self, input_bitmap: list) -> Image:
        pass

    @abstractmethod
    def from_image(self, input_image: Image) -> bytearray:
        pass
