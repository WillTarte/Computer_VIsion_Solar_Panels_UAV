#Author: William Tarte
#Purpose: given an input of an image, recognize if the solar panel has a lit IR beacon


##TODO: I'm able to extract the pixel values for the valleys but unable to choose the best one for thresholding
## Its possible the algorithm

#import necessary packages
import cv2
import numpy as np
from matplotlib import pyplot as plt


class Detection(object):

    def __init__(self, img_path):
        self.image_path = img_path
        self.image_matrix = self.calculate_matrix()
        self.histogram, self.bin_edges = self.calculate_histogram()
        self.peaks, self.valleys, self.gradient = self.histogram_differentiation()
        self.best_threshold, self.thresholds = self.threshold_calculation()

    def calculate_histogram(self):
        hist, bin_e = np.histogram(self.image_matrix, bins=range(self.image_matrix.min(),self.image_matrix.max()+1, 1))
        return hist, bin_e

    def calculate_matrix(self):
        img = cv2.imread(self.image_path, 0)
        img = cv2.GaussianBlur(img,(9,9),0)
        return np.matrix(img)

    def histogram_differentiation(self):
        differentiation = list()
        for i in range(len(self.histogram)-1):
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
        for i in range(len(gradient)-1):
            if gradient[i] == gradient[i+1]:
                continue
            elif gradient[i] > gradient[i+1]:
                peaks.append(i)
            elif gradient[i] < gradient[i+1]:
                valleys.append(i)

        return peaks, valleys, gradient

    def threshold_calculation(self):
        total = 0
        for i in self.valleys:
            total += self.histogram[i]
        mean = total / float(len(self.valleys))

        candidates = list()
        for index in self.valleys:
            freq = self.histogram[index]
            sq_diff = (self.gradient[index])**2
            d = np.ceil(abs(freq - mean + sq_diff))
            candidates.append(d)

        return min(candidates[1:len(candidates)-1]), candidates







test = Detection("C:\\Users\\Admin\\Documents\\My Stuff\\Programming\\Detecting Solar Panels\\Computer_VIsion_Solar_Panels_UAV\\images.jpg")
print(test.histogram, "\n", test.bin_edges)


print(test.peaks, "\n", test.valleys, "\n", test.gradient)
print(test.best_threshold,"\n", test.thresholds)

ret, thresh1 = cv2.threshold(cv2.imread(test.image_path), test.best_threshold, 255, cv2.THRESH_BINARY)
plt.imshow(thresh1)

plt.show()
