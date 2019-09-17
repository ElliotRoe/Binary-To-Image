import numpy as np
import math as m
from PIL import Image

binary = input("Input Binary here: ")

# gets approx width and height
# makes height always bigger in terms of rounding

h = m.ceil(m.sqrt(len(binary)))
w = round(m.sqrt(len(binary)))

# creates an array of RGB values full of zeros

data = np.zeros((h, w, 3), dtype=np.uint8)

# if array isn't exactly as big as binary data adds whitespace at the end
x = 0
if (len(binary) % w) != 0:
    while x < (w - (len(binary) % w)):
        data[h - 1, (w - 1) - x] = [0, 255, 0]
        x = x + 1

# Fills array with black and white pixels according to the 1s and 0s using row major order
x = 0
while x < len(binary):
    if binary[x] == '1':
        data[m.floor(x / w), x % w] = [255, 255, 255]
    elif binary[x] == ',':
        data[m.floor(x / w), x % w] = [0, 255, 0]

    x = x + 1
# turns array into image
img = Image.fromarray(data, "RGB")

# saves image
img.save("binary.png")
