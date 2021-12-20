def get_region(pixel, img, inf_char):
    terms = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    x_size, y_size = len(img[0]), len(img)
    x, y = pixel

    region = [
        img[y + ty][x + tx]
        if 0 <= x + tx <= x_size - 1 and 0 <= y + ty <= y_size - 1
        else inf_char
        for (tx, ty) in terms
    ]

    return region


def enhance_pixel(pixel, img, img_enhancement_alg, inf_char):
    region_str = "".join(get_region(pixel, img, inf_char)).translate(
        str.maketrans(".#", "01")
    )
    return img_enhancement_alg[int(region_str, 2)]


iea, img = open("input.txt", "r").read().split("\n\n")
img = [list(line) for line in img.splitlines()]

x_len, y_len = len(img[0]), len(img)
inf_char = "."

for i in range(50):
    # add top and bottom_border
    img =  [[inf_char] * x_len] * 2 + img + [[inf_char] * x_len] * 2
    y_len = len(img)

    # add left and right border  
    img = [[inf_char] * 2 + img[y] + [inf_char] * 2 for y in range(y_len)]  
    x_len = len(img[0])

    enhanced_img = []
    for y, row in enumerate(img):
        new_row = [enhance_pixel((x, y), img, iea, inf_char) for x in range(x_len)]
        enhanced_img.append(new_row)

    # update infinite char
    inf_char = iea[0] if inf_char == "." else iea[-1]
    
    img = enhanced_img


lit_pixel = sum([row.count("#") for row in img])
print(lit_pixel)

