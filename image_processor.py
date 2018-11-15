#Author: William Tarte
#Purpose: given an input of an image, recognize if the solar panel has a lit IR beacon


##TODO: Need to convert color images to grayscale. How do I check what color space the image is using?
##lastmin is not working

#import necessary packages
import cv2
import numpy as np
from matplotlib import pyplot as plt


class Detection(object):

    def __init__(self, img_path):
        self.image_path = img_path
        self.image_matrix = self.calculate_matrix()
        self.histogram, self.bin_edges = self.calculate_histogram()
        self.peaks, self.valleys, self.lastmin, self.lastmax = self.find_t()

    def calculate_histogram(self):
        hist, bin_e = np.histogram(self.image_matrix, bins=range(self.image_matrix.min(),self.image_matrix.max()+1, 1))
        return hist, bin_e

    def calculate_matrix(self):
        img = cv2.imread(self.image_path, 0)
        #img = cv2.GaussianBlur(img,(5,5),)
        return img

    def find_t(self):

        peaks = list()
        valleys = list()
        for index in range(0, len(self.bin_edges)-2):
            if self.histogram[index-1] > self.histogram[index] < self.histogram[index +1]:
                valleys.append(self.bin_edges[index])
            elif self.histogram[index-1] < self.histogram[index] > self.histogram[index +1]:
                peaks.append(self.bin_edges[index])
            else:
                continue

        lastmax = peaks[-1]

        i = len(valleys) - 1

        while valleys[i] >= lastmax:
            i = i - 1

        lastmin = valleys[i]

        return peaks, valleys, lastmin, lastmax


'''
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
'''







test = Detection("C:\\Users\\Admin\\Documents\\My Stuff\\Programming\\Detecting Solar Panels\\Computer_VIsion_Solar_Panels_UAV\\test4.jpg")


#print(test.lastmin)
#print(test.lastmax, '\n', test.valleys, '\n', test.peaks)

ret, thresh1 = cv2.threshold(test.image_matrix, test.lastmin , 255, cv2.THRESH_BINARY)


def results(d, t):
    coord = np.transpose(np.nonzero(t))

    connectivity = 4

    output = cv2.connectedComponentsWithStats(t, connectivity, cv2.CV_32S)

    num_l = output[0]
    labels = output[1]
    stats = output[2]
    centroids = output[3]

    for center in centroids:
        cv2.circle(d.image_matrix, (int(center[0]), int(center[1])), 4, (255), thickness=-1)

    cv2.imwrite('results3.png', d.image_matrix)
    return None

results(test, thresh1)
