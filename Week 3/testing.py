import numpy
import matplotlib
import pandas
from scipy import misc
from skimage import data
import matplotlib.pyplot as plt


photo_data = misc.imread('C:/Users/kevin/Documents/PyCharm/python-for-data-science/Week 3/sd-3layers.jpg')
print("Shape of photo_data:", photo_data.shape)
low_value_filter = photo_data < 0
print("Shape of low_value_filter:", low_value_filter.shape)\


plt.figure(figsize=(10,10))
plt.imshow(photo_data)
photo_data[photo_data < 200] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)

plt.show()