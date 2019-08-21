import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure(tight_layout=True)
length = 25
img = np.ones(shape=(length, length, 3))

plt.ion()
for i in range(length):
    im_show = img.copy()
    im_show[i] = 0
    plt.imshow(im_show)
    plt.pause(0.001)
plt.ioff()
plt.show()