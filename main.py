from lsb.encode_into import SimpleLSBEncoder

def encode():
    with open('test_input.txt', 'r', encoding='utf-8') as f:
        input_string = f.read()

    encoder = SimpleLSBEncoder('test_img.bmp', encoding='utf-8')
    encoder.encode(input_string)
    encoder.im.save('after_compression.bmp')
    #encoder.im.show()
    return encoder.bitlength

def decode(bl):
    encoder = SimpleLSBEncoder('after_compression.bmp', encoding='utf-8')
    encoder.bitlength = bl
    print(encoder.decode())

#bl = encode()
#decode(bl)

from glypher import .
