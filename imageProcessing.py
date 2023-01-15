import cv2
import numpy as np

def fetch_image():
    pass

def process_image(img_matrix):
    av_color_row = np.average(img_matrix, axis=0)
    av_color = np.average(av_color_row, axis=0)
    print(av_color)
