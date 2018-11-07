# Computer_VIsion_Solar_Panels_UAV

## TO-DO
	* The algorithm only checks adjacent pixel values to the right/down
	I have to change it so that it can check in every direction 
	* And divide the matrix by the total number of comparisons??
	* Gaussian bright detection works
	* _Have to find a way to check if the image has an IR bright spot. If it does,_
	_you apply the Gaussian bright detection._

## Current files
	*Some test images all labeled test(number).png // Only test.png has an IR bright spot
	* image_processor will be the code that detects solar panels. Currently Computes the GLCM of image (__BROKEN__)
	* Gaussian_bright_detection applies some preprocessing to the image and circles the IR emitter (_Brightest spot_)