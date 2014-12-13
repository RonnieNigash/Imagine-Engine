#from imagine-engine.colordefine import colordefine
#from imagine-engine.finder import finder
from colordefine import ColorDefine
from finder import Finder
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
colorDef = ColorDefine((8, 12, 3))


query = cv2.imread(args["query"])
features = colorDef.define(query)

finder = Finder(args["index"])
results = finder.find(features)

cv2.imshow("Query", query)

for (distance, fileName) in results:
    # loads the results images and dislay them
    result = cv2.imread(args["result_path"] + "/" + fileName)
    cv2.imshow("Result", result)
    cv2.waitKey()
