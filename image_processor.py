#Author: William Tarte
#Current Purpose: Detect the lit IR bright spot on an image of a solar panel

##TODO: Pre-proccess the image to get better detection
## Processing techniques: https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html


#import necessary packages
import cv2
import numpy as np
import argparse
import sys

#Class that does the image manipulation/holds the necessary information
class Detection(object):

    def __init__(self, img_path):

        self.image_path = img_path #String of the image path /// make sure it has double \\
        self.image_matrix = self.calculate_matrix() #Matrix representation of the grayscale image with preprocessing
        self.histogram, self.bin_edges = self.calculate_histogram() #Frequency values, left bin edges of the histogram
        self.peaks, self.valleys, self.lastmin, self.lastmax = self.find_t() #Pixel intensity values for peaks, values AND last valley value, last peak value

        #This thresholding uses my simple algorithm to find the best threshold value
        #It might be worth looking into Otsu's Method, Iterative Selection Thresholding Method and  balanced histogram thresholding method
        ret, self.thresh = cv2.threshold(self.image_matrix, self.lastmin , 255, cv2.THRESH_BINARY) #Applies thresholding to the input image

        self.detect()

    def calculate_histogram(self):
        """
        Calculates the input image's histogram and returns the pixel intensity
        frequency values and the left bin(category) edges
        """
        hist, bin_e = np.histogram(self.image_matrix, bins=range(self.image_matrix.min(),self.image_matrix.max()+1, 1))
        return hist, bin_e

    def calculate_matrix(self):
        """
        Reads the image in grayscale, and applies preprocessing.
        Returns the matrix representation (numpy) of the image.
        """
        img = cv2.imread(self.image_path, 0)
        img = cv2.GaussianBlur(img,(5,5),0)
        return img

    def find_t(self):
        """
        Iteratively combs through the histogram to find the best threshold value.
        Returns the valley/peak values and the last peak/valley(threshold).
        """
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

    def detect(self): #Need to optimize for better recognition.
        """
        Analyzes the thresholded image to find the components (IR spots in this case)
        and saves a copy of the original image with the IR spots highlighted.
        CURRENTLY NOT 100% EFFICIENT.
        """

        #Coordinates of all the non zero pixels
        coord = np.transpose(np.nonzero(self.thresh))

        CONNECTIVITY = 4 #Can be 4 or 8

        output = cv2.connectedComponentsWithStats(self.thresh, CONNECTIVITY, cv2.CV_32S) #This is a really whack OpenCV function

        #Which returns
        num_l = output[0] #The number of labels
        labels = output[1] #The labels themselves
        stats = output[2]   #The stats accessed with stats[label, column]
        centroids = output[3] #The center of the components

        #print(num_l)
        #print(labels)
        #print(stats)
        #print(centroids)

        copy = self.image_matrix.copy()

        copy = cv2.cvtColor(copy, cv2.COLOR_GRAY2BGR)
        for center in centroids[1:]:
            cv2.circle(copy, (int(center[0]), int(center[1])), 4, (255, 0, 0), thickness=-1)

        string = self.image_path.split("\\")[-1]
        components = string.split(".")
        name = components[0] + "_results" +"." + components[-1]

        cv2.imwrite(name, copy)
        return None

if __name__ == "__main__":

    try:
        parser = argparse.ArgumentParser(description="This is a python program to tag IR beacons on solar panels")

        parser.add_argument("path", action = 'store', type = str, help="You pass the image path as an argument")

        args = parser.parse_args()

        if args.path:
            try:
                IR_detection = Detection(args.path.encode('unicode_escape').decode())
                print("Code ran without problem")
            except Exception as e:
                print("Encountoured an exception of type:", e)
                sys.exit()
            else:
                sys.exit()
        else:
            print("Please input a path to an image to process")
            sys.exit()
    except Exception as e:
        print("Encountered exception of type:", e)
        sys.exit()
    else:
        sys.exit()
