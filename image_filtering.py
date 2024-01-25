"""
CS 4391 Homework 1 Programming
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# main function
if __name__ == '__main__':
    # Step 1: read the crack box image with cv2.imread
    im = None


    # Step 2: use cv2.cvtColor to convert RGB image to gray scale image 
    #(replace with your code)
    gray_image = None


    # Step 3: define the filter kernel as described in the homework description as a numpy array
    #(replace with your code)
    kernel = None


    # Step 4: filter the image with the kernel
    #(replace with your code)
    output = None


    # show result with matplotlib (no need to change code below)
    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(gray_image, cmap = 'gray')
    ax.set_title('Original image')

    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(output, cmap = 'gray')
    ax.set_title('Filtered image')

    plt.show()
