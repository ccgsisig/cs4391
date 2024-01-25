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
    

    # Step 3: use central difference to compute image gradient on the gray scale image
    #(replace with your code)
    gradient_x = None
    gradient_y = None


    # show result with matplotlib (no need to change code below)
    fig = plt.figure()
    ax = fig.add_subplot(1, 3, 1)
    plt.imshow(gray_image, cmap = 'gray')
    ax.set_title('Original image')

    ax = fig.add_subplot(1, 3, 2)
    plt.imshow(gradient_x, cmap = 'gray')
    ax.set_title('Gradient X')

    ax = fig.add_subplot(1, 3, 3)
    plt.imshow(gradient_y, cmap = 'gray')
    ax.set_title('Gradient Y')

    plt.show()
