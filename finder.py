import numpy
import csv

class Finder:
    def find(self, similarFeatures, limit = 10):

        # dictionary with:
        #           unique fileName for keys
        #           similarity to input image for values
        results = {}

        with open(self.indexPath) as file:

            reader = csv.reader(file)

            for row in reader:

                features = [float(x) for x in row[1:]]
                distance = self.chi2_distance(features, queryFeatures)
