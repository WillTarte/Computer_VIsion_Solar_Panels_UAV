#Author: William Tarte
#Purpose: given an input of an image, recognize solar panels

'''
Algorithm:
1. Load image using open CV
2. Convert image to grayscale values
3. Calculate constants: range of grayscale values (p), size of image
4. Generate matrix of image
5. Generate co occurence matrix of image (with given offset)
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
co_matrix = np.zeros((dimension_co,dimension_co),dtype=int)

print(img)
print(co_matrix)
x_offset = 1
y_offset = 1
img_x = 0
img_y = 0
co_x = 0
co_y = 0

start_loc = [0,0]


while True:
    for x in range(x_offset+1):
        for y in range(y_offset+1):
            if img[start_loc[0]][start_loc[1]] == img[start_loc[0]+x][start_loc[1]+y]:
                co_matrix[co_x][co_y] +=1

    start_loc = [start_loc[0]+x_offset, start_loc[1]+y_offset]
    co_x += 1
    if co_x >= dimension_co:
        co_x = 0
        co_y +=1
        if co_y >= dimension_co:
            break

print(co_matrix)






'''
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
