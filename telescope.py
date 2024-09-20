import random

import matplotlib.pyplot as plt
import numpy as np


# ------------------------------
# Define a class named telescope
# ------------------------------
class telescope:
    # initialization function
    def __init__(self, resolution):
        self.resolution = resolution  # ATTRIBUTE

    # METHOD
    def observe(self):
        image = np.empty(shape=(self.resolution, self.resolution))
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                image[i, j] = random.random()

        return image


# create two objects of type telescope with different resolution
telescope1 = telescope(100)
telescope2 = telescope(resolution=200)

# call observe on each object to get two images
image1 = telescope1.observe()
image2 = telescope2.observe()

fig, ax = plt.subplots(1, 2)
ax[0].imshow(image1)
ax[0].set_title("Telescope 1")
ax[1].imshow(image2)
ax[1].set_title("Telescope 2")
plt.show()
