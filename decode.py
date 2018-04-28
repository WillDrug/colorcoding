from encode import mark_0, mark_1, mark_2
def bitmap_from_image(im):
    px = im.load()
    bmp = list()
    for i in range(im.size[0]):
        row=list()
        for j in range(im.size[1]):
            row.append(px[i, j])
        bmp.append(row)
    return bmp

def text_from_bitmap(bm):
    output_array = bytearray()
    for row in bm:
        for px in row:
            if px[2] == mark_2:
                output_array.append(px[0])
                output_array.append(px[1])
            elif px[2] == mark_1:
                output_array.append(px[0])
            elif px[2] == mark_0:
                continue
            else:
                print('Wrong encoding origin! Exiting')
                exit()
    return output_array[::-1]