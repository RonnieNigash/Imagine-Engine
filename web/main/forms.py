from django import forms

class ImageForm(forms.Form):
	image = forms.FileField(label = "Select an input Image to compare images against")

