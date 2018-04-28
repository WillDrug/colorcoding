import sys
from PIL import Image
from encode import generate_bitmap, generate_image
from decode import bitmap_from_image, text_from_bitmap
#f = open('input_string.txt', 'r+', encoding='utf-8')
#input_string = f.readline()
#f.close()
input_string = sys.argv[1]
print(f'Encoding {input_string}')
output_map = generate_bitmap(input_string)
im = generate_image(output_map)
im.show()
decode_map = bitmap_from_image(im)
decode_array = text_from_bitmap(decode_map)
print(decode_array.decode('utf-8'))

"""
im = Image.open('input_img.bmp')

f = open('input_string.txt', 'r+', encoding='utf-8')
input_string = f.readline()
f.close()
input_bytes = bytearray(input_string.encode('utf-8'))

full_size = im.size[0]*im.size[1]
if full_size < input_bytes.__len__():
    print('Input file is too large')
    exit(1)

pixel_map = im.load()
string_img = list()
for i in range(im.size[0]):
    for j in range(im.size[1]):
        string_img.append(pixel_map[i, j])

skip_num = int(string_img.__len__()/input_bytes.__len__())
it = input_bytes.__iter__()
for i in range(0, string_img.__len__(), skip_num):
    try:
        bt = it.__next__()
        string_img[i] = (bt, string_img[i][1], string_img[i][2])
    except StopIteration:
        pass

string_img = string_img[::-1]

for i in range(im.size[0]):
    for j in range(im.size[1]):
        pixel_map[i, j] = string_img.pop()

im.show()"""