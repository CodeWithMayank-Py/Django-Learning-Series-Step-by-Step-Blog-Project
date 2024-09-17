from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.generic import ListView

# Create your views here.

# Function Bassed Views

# Display all Blogs
def index(request):
    display_blogs = Blog.objects.all()
    return HttpResponse(display_blogs)


# Class based View
class BlogListView(ListView):
    model = Blog
    def get(self, request, *args, **kwargs):
        blogs = Blog.objects.all()
        return HttpResponse(blogs)