from django.db import models

# Create your models here.

class Image(models.Model):
	imgfile = models.FileField(upload_to='documets/%Y/%m/%d')

class InputImage(models.Model):
	input_image_file_path = models.CharField(max_length = 50)

class FoundImages(models.Model):
	input_image = models.ForeignKey(InputImage)
	output_image_file_path = models.CharField(max_length = 50)