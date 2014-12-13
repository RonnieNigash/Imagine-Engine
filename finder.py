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

            # rows contain fileName and feature values and
            for row in reader:

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
