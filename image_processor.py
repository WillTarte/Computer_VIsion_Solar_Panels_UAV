#Author: William Tarte
#Purpose: given an input of an image, recognize solar panels

'''
Algorithm:
1. Load image using open CV
2. Convert image to grayscale values
3. Calculate constants: range of grayscale values (p), size of image
4. Generate matrix of image
5. Generate co occurence matrix of image (with given offset)
    a) check image pixel at (x,y) check all pixels within offsets (left,right,top,down,diagonals)
    b) if the grayscale intensity is within threshold, add 1 to co occurence matrix at (x,y)
    c) when done checking, co occurence (x,y+1)
        if at the end of the row, co occurence (x+1, y=0)
        if index x out of bounds, break
    d) start again starting at pixel (x, y + offset)
        if at the end of the row or higher, image matrix (x+1, y=0)
        if x index is at the end or out of bounds, break

'''
import cv2
import numpy as np
import matplotlib as mpl

#load image in grayscale
img = cv2.imread("C:\\Users\\Admin\\Documents\\My Stuff\\Programming\\Detecting Solar Panels\\Computer_VIsion_Solar_Panels_UAV\\test.png", 0);

#make img a numpy array
img_matrix = np.matrix(img)

#finding upper bound
p_max = np.max(img_matrix)
#find lower bound
p_min = np.min(img_matrix)

dimension_co = p_max - p_min
#initializing co occurence img_matrix
co_matrix = np.zeros((dimension_co,dimension_co),dtype=np.int32)

print(img)
x_offset = 2
y_offset = 2
img_x = 0
img_y = 0
co_x = 0
co_y = 0

start_loc = [0,0]
threshold = 5

while True:
    for x in range(0, x_offset):
        for y in range(0, y_offset):
            if abs(int(img[start_loc[0]][start_loc[1]]-img[start_loc[0]+x][start_loc[1]+y])) <= threshold:
                co_matrix[co_x][co_y] +=1
                continue

    start_loc[0] += x_offset
    if start_loc[0] > img_matrix.shape[0]-x_offset:
        start_loc[0] = 0
        start_loc[1] += y_offset
        if start_loc[1] > img_matrix.shape[1]-y_offset:
            break

    co_x += 1
    if co_x >= dimension_co:
        co_x = 0
        co_y +=1
        if co_y >= dimension_co:
            break


print(co_matrix[0])







cv2.imshow('image',img)
cv2.imshow('GLCM', co_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()
