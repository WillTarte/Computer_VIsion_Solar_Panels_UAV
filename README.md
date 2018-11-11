# Computer_VIsion_Solar_Panels_UAV

## TO-DO
* The algorithm only checks adjacent pixel values to the right/down
I have to change it so that it can check in every direction
* And divide the matrix by the total number of comparisons??
* Gaussian bright detection works
* _Have to find a way to check if the image has an IR bright spot. If it does,_
_you apply the Gaussian bright detection._

## Current files
* Some test images all labeled test(number).png // Only test.png has an IR bright spot
* image_processor will be the code that detects solar panels. Currently Computes the GLCM of image (__BROKEN__)
* Gaussian_bright_detection applies some preprocessing to the image and circles the IR emitter (_Brightest spot_)

## Sources
* https://www.scnsoft.com/blog/machine-vision-to-detect-solar-panel-defects
* https://en.wikipedia.org/wiki/DBSCAN#Algorithm
* https://www.pyimagesearch.com/2014/09/29/finding-brightest-spot-image-using-python-opencv/
* https://support.echoview.com/WebHelp/Windows_and_Dialog_Boxes/Dialog_Boxes/Variable_properties_dialog_box/Operator_pages/GLCM_Texture_Features.htm
* https://www.pyimagesearch.com/2017/08/21/deep-learning-with-opencv/
* https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606
* https://www.researchgate.net/publication/318694161_On_the_detection_of_solar_panels_by_image_processing_techniques
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3386707/
