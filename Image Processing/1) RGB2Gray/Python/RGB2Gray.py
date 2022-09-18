import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image
import cv2
import numpy as np


def Entry(input):
    arr = cv2.imread(input)
    arr = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB) # convert simple image to 3 channel RGB format
    plt.imshow(arr)
    plt.title('my image')
    plt.show()
    return arr

"""
dot product of Array and the luminance of gray RGB,
which can be modified easily by setting different numbers
"""
def RGB_Gray(arr):
    gray= np.dot(arr, [0.299, 0.587, 0.114]) 
    plt.title('Gray Scale image')
    plt.imshow(gray, cmap="gray")
    plt.show()


def RGB_Red(arr):
    red = arr.copy()
    red[:, :, 1]= 0
    red[:, :, 2]= 0
    plt.title('Red Channel')
    plt.imshow(red)
    plt.show()


def RGB_Green(arr):
    green= arr.copy()
    green[:, :, 0]= 0
    green[:, :, 2]= 0
    plt.title('Green Channel')
    plt.imshow(green)
    plt.show()


def RGB_Blue(arr):
    blue= arr.copy()
    blue[:, :, 0]= 0
    blue[:, :, 1]= 0
    plt.title('Blue Channel')
    plt.imshow(blue)
    plt.show()





