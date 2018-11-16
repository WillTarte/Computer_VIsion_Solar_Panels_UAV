# Computer_VIsion_Solar_Panels_UAV

## TO-DO


## Current files
* All the test Images and the results of applying the algorithm
* image_processor.py which contains the Detection class
* Random_code folder which has code that's not currently useful but that I don't want to get rid of

## Sources
Solar Panel Defect Detection with Machine Vision
DBSCAN - Wikipedia
Finding the Brightest Spot in an Image using OpenCV
GLCM Texture Feature
Deep Learning with OpenCV - PyImageSearch
Object Detection with 10 lines of code – Towards Data Science
(PDF) On the detection of solar panels by image processing techniques
Using the Standard Deviation of a Region of Interest in an Image to Estimate Camera to Emitter Distance
Image Analysis - Intensity Histogram
python - histogram of gray scale values in numpy image - Stack Overflow
background subtraction - Differences between MOG, MOG2, and GMG - Stack Overflow
Blob Detection Using OpenCV ( Python, C++ ) | Learn OpenCV
OpenCV: Background Subtraction
Blob detection with k-means part 1 - YouTube
Adaptive histogram equalization - Wikipedia
Adaptive histogram equalization - Wikipedia
What is the meaning of 'min-max normalization'? - Quora
Histogram equalization - Wikipedia
(PDF) Fault Diagnosis of Photovoltaic Modules through Image Processing and Canny Edge Detection on Field Thermographic Measurements
python - Plot two histograms at the same time with matplotlib - Stack Overflow
OpenCV: Image Thresholding
(PDF) A simple approach to determine the best threshold value for automatic image thresholding
python - numpy histogram cumulative density does not sum to 1 - Stack Overflow
Grayscale - Wikipedia
Detecting multiple bright spots in an image with Python and OpenCV - PyImageSearch
Drawing a colored rectangle in a grayscale image using opencv - Stack Overflow
OpenCV: Drawing Functions in OpenCV




### Interesting idea from previous link
  1. Step 1: Read the thermal image I;
  2. Step 2: Smooth I using convolution by a 1D Gaussian G mask;
  3. Step 3: Create a 1D mask for the ﬁrst derivative of the Gaussian in the x- and y-directions;
  4. Step 4: Convolve I with G along the rows to obtain Ixand down the columns to obtain Iy;
  5. Step 5: Convolve Ixwith Gxto have gxand Iywith Gyto have gy;
  6. Step 6: Find the magnitude M and the angle θ of the result at each pixel (x,y);
  7. Step 7: Preserve all local maxima in the gradient image and mark them as edges;
  8. Step 8: Apply hysteresis thresholding; Edge pixels stronger than the upper threshold aremarked as ‘strong’, edge pixels weaker than the lower threshold are suppressed and edgepixels between the two thresholds are marked as weak;
  9. Step 9: Final edges are determined by suppressing all edges that are not connected to a strongedge. 

(PDF) Fault Diagnosis of Photovoltaic Modules through Image Processing and Canny Edge Detection on Field Thermographic Measurements. Available from: https://www.researchgate.net/publication/247160766_Fault_Diagnosis_of_Photovoltaic_Modules_through_Image_Processing_and_Canny_Edge_Detection_on_Field_Thermographic_Measurements [accessed Nov 11 2018].
