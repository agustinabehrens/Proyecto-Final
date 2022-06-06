from django.http import HttpResponse
from django.views.generic import TemplateView,CreateView
from Blog.models import Post
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'index.html'



