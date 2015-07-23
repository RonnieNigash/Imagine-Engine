from django import forms

class ImageForm(forms.Form):
	imgfile = forms.FileField(
			label = 'Select an image')
