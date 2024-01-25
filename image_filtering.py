"""
CS 4391 Homework 1 Programming
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# main function
if __name__ == '__main__':
    # Step 1: read the crack box image with cv2.imread
    im = cv2.imread('cracker_box.jpg')


    # Step 2: use cv2.cvtColor to convert RGB image to gray scale image 
    #(replace with your code)
    gray_image = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


    # Step 3: define the filter kernel as described in the homework description as a numpy array
    #(replace with your code)
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])


    # Step 4: filter the image with the kernel
    #(replace with your code)
    output = cv2.filter2D(gray_image, -1, kernel)


    # show result with matplotlib (no need to change code below)
    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(gray_image, cmap = 'gray')
    ax.set_title('Original image')

    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(output, cmap = 'gray')
    ax.set_title('Filtered image')

    plt.show()
