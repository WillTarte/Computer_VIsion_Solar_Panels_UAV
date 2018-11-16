# Computer_VIsion_Solar_Panels_UAV

## TO-DO


## Current files
* All the test Images and the results of applying the algorithm
* image_processor.py which contains the Detection class
* Random_code folder which has code that's not currently useful but that I don't want to get rid of

## Sources
* https://www.scnsoft.com/blog/machine-vision-to-detect-solar-panel-defects
* https://en.wikipedia.org/wiki/DBSCAN#Algorithm
* https://www.pyimagesearch.com/2014/09/29/finding-brightest-spot-image-using-python-opencv/
* https://support.echoview.com/WebHelp/Windows_and_Dialog_Boxes/Dialog_Boxes/Variable_properties_dialog_box/Operator_pages/GLCM_Texture_Features.htm
* https://www.pyimagesearch.com/2017/08/21/deep-learning-with-opencv/
* https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606
* https://www.researchgate.net/publication/318694161_On_the_detection_of_solar_panels_by_image_processing_techniques
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3386707/
* https://www.researchgate.net/publication/247160766_Fault_Diagnosis_of_Photovoltaic_Modules_through_Image_Processing_and_Canny_Edge_Detection_on_Field_Thermographic_Measurements




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
