import numpy
import cv2

class ColorDefine:
    def define(self, image):
        # changes image to Hue/Saturation/Value color space
        # from the RGB (backwards = BGR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # empty list to later be filled with definition of image
        # photos defined with:
        #    (volume of Hue/Saturation/Value color space) floats
        #    each float describes a pixel's position (HSV value) in color space
        features = []

        (height, width) = image.shape[:2]
        (centerWidth, centerHeight) = (int(width * 0.5), int(height * 0.5))

        # localizing color distribution with five regions
        regions = [(0, centerWidth, 0, centerHeight),
                    (centerWidth, width, 0, centerHeight),
                    (centerWidth, width, centerHeight, height),
                    (0, centerWidth, centerHeight, height)]

        # circular region (more of an ellipse) for focus of image
        (xAxis, yAxis) = (int(width * 0.75) / 2 , int(height * 0.75) / 2)
        ellipseMask = numpy.zeros(image.shape[:2], dtype = "uint8")
        cv2.ellipse(ellipseMask, (centerWidth, centerHeight), (xAxis, yAxis),
                    0, 0, 360, 255, -1)

        for (startX, endX, startY, endY) in regions:
            # creating mask for four corner regions of image
            cornerMask = numpy.zeros(image.shape[:2], dtype = "uint8")
            cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
            cornerMask = cv2.subtract(cornerMask, ellipseMask)

            # take image data from more focused image (region)
            tempHist = self.histogram(image, cornerMask)
            features.extend(tempHist)

        # now take data from center elliptical region

        tempHist = self.histogram(image, ellipseMask)
        features.extend(tempHist)

        return features;

    def histogram(self, image, mask):
        # take the Hue/Saturation/Value data from a masked region and
        # normalize (use percentages values) histogram to compare
        # images of different proportion and size but same data (content)
        hist = cv2.calcHist([image], [0, 1, 2], mask, self.colorHistogramBars,
                [0, 180, 0, 256, 0, 256])
        hist = cv2.normalize(hist)

        return hist


    def __init__(self, colorHistogramBars):
        self.colorHistogramBars = colorHistogramBars
