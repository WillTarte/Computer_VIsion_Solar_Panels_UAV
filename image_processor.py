#Author: William Tarte
#Purpose: given an input of an image, recognize solar panels

'''
Algorithm:
1. load image in with opencv (In Grayscale)
2. Create numpy matrix of image and calculate dimensions of co_matrix (range of pixels in original image)
3. Create numpy matrix for GLCM filled with 0's
4. For given off_sets (vector(x,y)), pass through the image co_matrix
    a) for each pair of pixel values at (start location, start location + offset),
       add 1 in the occurrence matrix for that value pair
    b) if you reach the end of the row, set column to 0 and continue on next row
    c) if you reach the end of the row, and you're in the last column, break
5. Display co_occurence matrix. Display Histogram ##TODO
'''

##TODO: Fix the code that calculates the GLCM (keep getting index errors)

#import necessary packages
import cv2
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

#load image in grayscale
img = cv2.imread("C:\\Users\\Admin\\Documents\\My Stuff\\Programming\\Detecting Solar Panels\\Computer_VIsion_Solar_Panels_UAV\\test.png", 0);

#make img a numpy array
img_matrix = np.matrix(img)

#find max pixel value
p_max = np.max(img_matrix)
#find minimum pixel value
p_min = np.min(img_matrix)

#Calculating dimensions and initializing GLCM
dimension_co = p_max - p_min
co_matrix = np.zeros((dimension_co,dimension_co),dtype=np.int32)

#This is the offset vector
x_offset = 1
y_offset = 1

#row, column
start_loc = [0,0]

#test code
print(img_matrix.shape)
print(img_matrix.shape[0], img_matrix.shape[1])
# shape (129, 145)

#how to access numpy array/matrix values :^)
#img_matrix[0,0]


#Main loop for GLCM computation
while True:

    print(start_loc)

    #this tests if we are at the end of rows/columns
    if start_loc[1] >= img_matrix.shape[1]:
        start_loc[1] = 0
        start_loc[0] += x_offset
        if start_loc[0] >= img_matrix.shape[0]:
            break

    #With given offsets, create all possible vectors (in this case checks up to 9 neighbours
    #for each pixel
    for x in range(-x_offset, x_offset +1):
        #check to see if neigbour pixel is inside matrix
        if (start_loc[0] + x < 0) or (start_loc[0] + x >= co_matrix.shape[0]):
            continue
        for y in range(-y_offset, y_offset+1):
            if (start_loc[1] + y <= 0) or (start_loc[1] + y >= co_matrix.shape[1]):
                continue
            print("vector(",x,", ",y,")")

            #if it is, then find the pixel values and increment their combination in the GLCM
            p_pair = [img_matrix[start_loc[0], start_loc[1]], img_matrix[start_loc[0]+x, start_loc[1]+y]]
            co_matrix[p_pair[0]-p_min, p_pair[1]-p_min] += 1

    #start from the next pixel
    start_loc[1] += y_offset

#Code below to display results

cv2.imshow('image',img)

a = co_matrix.copy()
a = a.astype(np.uint8)
a = np.expand_dims(a, axis = 2)
a = np.concatenate((a, a, a), axis = 2)
print(a.shape)
plt.imshow(a)
plt.show()

cv2.waitKey(0)
plt.close('all')
cv2.destroyAllWindows()
