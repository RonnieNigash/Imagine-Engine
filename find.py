from imagine-engine.colorDefine import colorDefine
from imagine-engine.finder import finder
import argparse
import cv2

argp = argparse.ArgumentParser()
argp.add_argument("-i", "--index", required = True,
    help = "Path to where the computed index will be stored")
argp.add_argument("-q", "--query", required = True,
    help = "Path to the query image")
argp.add_argument("-r", "--result-path", required = True,
    help = "Path to the result path")
args = vars(argp.parse_args())

# initializing with same number of color histogram bars
cd = ColorDefine((8, 12, 3))
