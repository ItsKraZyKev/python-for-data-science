import numpy as np
import matplotlib
import pandas
from scipy import misc
from skimage import data
import matplotlib.pyplot as plt

photo_data = misc.imread('C:/Users/kevin/Documents/PyCharm/python-for-data-science/Week 3/sd-3layers.jpg')

red_mask = photo_data[:, :, 0] < 200  # red
green_mask = photo_data[:, :, 1] < 200  # green
blue_mask = photo_data[:, :, 2] < 200  # blue

final_mask = np.logical_and(red_mask, green_mask, blue_mask)
photo_data[final_mask] = 0
plt.figure(figsize=(15, 15))
plt.imshow(photo_data)

plt.show()
