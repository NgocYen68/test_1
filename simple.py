import cv2
import numpy as np

data = np.zeros([60, 60, 3])
h, w, c = data.shape

color_map = [
    (255, 0, 0), # blue
    (0, 255, 0), # green
    (0, 0, 255), # red
    (0, 0, 0), # black
    (255, 255, 255), # white
    (100, 100, 100), # grey
    (120, 50, 10),
    (36, 167, 227),
    (240, 212, 0),
]

assert h == w
step = h // 3
i = 0
for row in range(3):
    for col in range(3):
        data[row*step:(row+1)*step, col*step:(col+1)*step, :] = color_map[i]
        i += 1

cv2.imwrite("simple.png", data)
print("Done writing image: simple.png")