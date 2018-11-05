#Author: William Tarte
#Purpose: given an input of an image, recognize solar panels

'''
Algorithm:
1. load image in with opencv (In Grayscale)
2. Create numpy matrix of image and calculate dimensions of co_matrix
3. Create numpy matrix for GLCM filled with 0's
4. For given off_sets (vector(x,y)), pass through the image co_matrix
    a) for each pair of pixel values at (start location, start location + offset),
       add 1 in the occurrence matrix for that value pair
    b) if you reach the end of the row, set column to 0 and continue
    c) if you reach end of a column, that means you went through whole img_matrix, break
5. Display co_occurence matrix


'''
import cv2
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

#load image in grayscale
img = cv2.imread("C:\\Users\\Admin\\Documents\\My Stuff\\Programming\\Detecting Solar Panels\\Computer_VIsion_Solar_Panels_UAV\\test3.png", 0);

#make img a numpy array
img_matrix = np.matrix(img)

#finding upper bound
p_max = np.max(img_matrix)
#find lower bound
p_min = np.min(img_matrix)

dimension_co = p_max - p_min
#initializing co occurence img_matrix
co_matrix = np.zeros((dimension_co,dimension_co),dtype=np.int32)


x_offset = 2
y_offset = 2
img_x = 0
img_y = 0
co_x = 0
co_y = 0

start_loc = [0,0]

while True:

    if start_loc[1] >= img_matrix.shape[0]- y_offset:
        start_loc[1] = 0
        start_loc[0] += x_offset
        if start_loc[0] >= img_matrix.shape[0]- x_offset:
            break

    for x in range(0, x_offset):
        for y in range(0, y_offset):
            p_value = [img_matrix.item((start_loc[0],start_loc[1])), img_matrix.item((start_loc[0]+x_offset, start_loc[1] +y_offset))]
            co_matrix.itemset((p_value[0] - p_min - 1, p_value[1]-p_min - 1), co_matrix.item((p_value[0] - p_min - 1, p_value[1]-p_min - 1))+1)

    start_loc[1] += y_offset

cv2.imshow('image',img)

a = co_matrix.copy() # Replace this line with your 90x100 numpy array.
a = a.astype(np.uint8)
a = np.expand_dims(a, axis = 2)
a = np.concatenate((a, a, a), axis = 2)
print(a.shape)
plt.imshow(a)
plt.show()


cv2.waitKey(0)
plt.close('all')
cv2.destroyAllWindows()
