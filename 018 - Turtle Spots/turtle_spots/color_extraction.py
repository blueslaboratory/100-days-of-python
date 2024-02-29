# 22/02/2024
# Day - 018


# https://pypi.org/project/colorgram.py/
# pip install colorgram.py

##################################################
print("\n\n*** Hirst spot painting ***")

import colorgram

color_rgb_list = []
colors = colorgram.extract(".\\018\\turtle_spots\\hirst-spot-painting.jpg", 21)

# print(colors)


for c in range(len(colors)):
    # print(c, "-", colors[c].rgb)
    
    r = colors[c].rgb.r
    g = colors[c].rgb.g
    b = colors[c].rgb.b
    
    rgb_tuple = (r, g, b)
    
    color_rgb_list.append(rgb_tuple)
    

print("color_rgb_list:", color_rgb_list)


# copied from the terminal:
color_list = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 232, 237), (146, 28, 66), (239, 75, 35), (230, 237, 232), (7, 148, 94), (220, 171, 45), (182, 159, 48), (44, 191, 232), (28, 126, 194), (253, 223, 0), (125, 192, 79), (84, 28, 91), (245, 219, 50), (179, 40, 98), (42, 169, 116), (209, 131, 165), (205, 56, 35), (239, 161, 192)]