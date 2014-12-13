import cv2
import numpy

class ColorDefine:
    def __ init__(self, colorHistogramBars):
        self.colorHistogramBars = colorHistogramBars

    def describe(self, image):
        # changes image to Hue/Saturation/Value color space
        # from the RGB (backwards = BGR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # empty list to later be filled with definition of image
        # photos defined with:
        #    (volume of Hue/Saturation/Value color space) floats
        #    each float describes a pixel's position (HSV value) in color space
        features = []
