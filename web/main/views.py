from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView

from .forms import ImageForm
from .models import Image

class ImageView(FormView):
	template_name = 'main/uploaded_image_form.html'
	form_class = ImageForm

	def form_valid(self, form):
		uploaded_image = Image(
				image = self.get_form_kwargs().get('files')['image'])
		uploaded_image.save()
		self.id = uploaded_image.id

		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		return reverse('uploaded_image', kwargs = {'pk' : self.id})


class DetailView(DetailView):
	model = Image
	template_name = 'main/uploaded_image.html'
	context_object_name = 'image'

class ImageIndexView(ListView):
	model = Image
	template_name = 'main/uploaded_image_view.html'
	context_object_name = 'images'
	queryset = Image.objects.all()
