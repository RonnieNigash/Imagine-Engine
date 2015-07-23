from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from webUI.search.models import Image 
from webUI.search.forms import ImageForm

def index(request):
	return HttpResponse("Search index page.")

