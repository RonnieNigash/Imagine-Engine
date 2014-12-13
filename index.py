from imagine-engine.colordefine import ColorDefine
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
