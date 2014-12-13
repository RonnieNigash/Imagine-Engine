Imagine-Engine
==============

Image Search Engine
===================

This is a reverse image search engine written in python. Using a dataset of .png images it creates histograms of colors to compare the query image against. Too often we have to deal with sorting through thousands of family photos come the holidays. This python script should cut down that time with very little to no time investment. Don't bother tagging all of your images when you can visually search your database! Simply choose an image that looks close to what you want and send it through the script.

Usage
=====
```$ python index.py --dataset <directory path to dataset of images> --index index.csv```

^^ creates an index.csv files that will be used to index the entire dataset of images

```$ python find.py --index index.csv --query <directory path to input image> --result-path <directory path to dataset of images>```

^^ returns the top ten (max) images from the dataset that are closest in matching the input image


Issues
======


Make sure to install numpy

'''$ pip install numpy```

and OpenCv

```brew install opencv```
