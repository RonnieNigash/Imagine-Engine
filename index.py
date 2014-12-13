from colordefine import ColorDefine
import cv2
import argparse
import glob

# things we want when our method is called
argp = argparse.ArgumentParser()
argp.add_argument("-d", "--dataset", required = True,
    help = "Path to the directory that contains the image to be indexed")
argp.add_argument("-i", "--i", required = True,
    help = "Path to where the computed index will be stored")
args = vars(argp.parse_args())

# 8 Hue bars, 12 Saturation bars, 3 Value bars
colorDef = ColorDefine((8, 12, 3))

# starts output index file for writing to
outputFile = open(args["index", "w"])


for imagePath in glob.glob(args["dataset" + "/*.png"]):
    # take the file name and load the image using cv2
    imageFileName = imagePath[imagePath.rfind("/") + 1:]
    image = cv2.imread(imagePath)

    features = colorDef.define(image)

    # write how we have defined the file
    features = [str(f) for f in features]
    outputFile.write("%s,%s\n" % (imageFileName, ",".join(features)))

outputFile.close()
