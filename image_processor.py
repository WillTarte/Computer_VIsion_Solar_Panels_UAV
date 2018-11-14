#Author: William Tarte
#Purpose: given an input of an image, recognize if the solar panel has a lit IR beacon


##TODO:
##      Perform gradient analysis to determine best threshold value

#import necessary packages
import cv2
import numpy as np


class Detection(object):

    def __init__(self, img_path):
        self.image_path = image_path
        self.image_matrix = self.calculate_matrix()
        self.histogram, self.bin_edges = self.calculate_histogram()
        self.peaks, self.valleys = histogram_differentiation()

    def calculate_histogram(self):
        hist, bin_e = np.histogram(self.image_matrix, bins=range(self.image_matrix.min(),self.image_matrix.max()+1, 1))
        return hist, bin_e

    def calculate_matrix(self):
        img = cv2.imread(self.image_path, 0)
        return np.matrix(img)

    def histogram_differentiation(self):
        differentiation = list()
        for i in (len(self.histogram)-2):
            differentiation.append(self.histogram[i+1] - self.histogram[i])
        differentiation.append(0)

        gradient = list()
        for val in differentiation:
            if val == 0:
                gradient.append(0)
            elif val > 0:
                gradient.append(1)
            elif val < 0:
                gradient.append(-1)

        peaks = list()
        valleys = list()
        for i in len(gradient)-2):
            if gradient[i] == gradient[i+1]:
                continue
            elif gradient[i] > gradient[i+1]:
                peaks.append(i)
            elif gradient[i] < gradient[i+1]:
                valleys.append(i)

        return peaks, valleys
