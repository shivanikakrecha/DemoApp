from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def PostListing(request):
	return HttpResponse('<h1>Page was found</h1>')
