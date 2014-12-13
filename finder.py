import numpy
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import csv

class Finder:
    def find(self, similarFeatures, limit = 10):

        # dictionary with:
        #           unique fileName for keys
        #           similarity to input image for values
        results = {}

        with open(self.fileName) as file:

            reader = csv.reader(file)

            # rows contain fileName and feature values and
            for row in reader:
                print "We are here"

                features = [float(x) for x in row[1:]]
                distance = self.chi2_distance(features, similarFeatures)
                # compares the distance between features in index
                # and our input features

                results[row[0]] = distance

            file.close()

        # smaller distances are images with more similar values
        # smaller distances are put at the front of dictionary
        results = sorted([(value, key) for (key, value) in results.items()])

        # based on passed parameter, return "limit" amount of results
        return results[:limit]


    def chi2_distance(self, histogramA, histogramB, epsilon = 1e-10):
        # takes both histograms we are comparing
        # epsilon prevents division by zero if the images are identical
        distance = 0.5 * numpy.sum([((a - b) ** 2) / (a + b + epsilon)
                for (a, b) in zip(histogramA, histogramB)])

        return distance

    def __init__(self, fileName):
        self.fileName = fileName
