from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from search.models import Image
from search.forms import ImageForm

def list(request):
	if request.method == "POST":
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			newimg = Image(docfile = request.FILES["imgfile"])
			newimg.save()

			return HttpResponseRedirect(reverse("webUI.views.input"))
		else:
			form = ImageForm()
	
	images = Form.objects.all()

	return render_to_response("webUI/input.html", 
			{'images' : images, "form" : form}, 
			context_instance = RequestContext(request))

def index(request):
	return HttpResponse("Search index page.")

