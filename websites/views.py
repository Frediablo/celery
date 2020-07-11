from django.shortcuts import render, get_object_or_404
from .models import Website, WebsiteCategory, WebPage
from django.views.generic import ListView, DetailView, CreateView
from .forms import WebsiteModelForm


# Create your views here.
class WebsiteListView(ListView):
    model = Website
    template_name = 'websites/websites.html'


class WebsiteDetailView(DetailView):
    pass


class CreateWebsite(CreateView):
    form_class = WebsiteModelForm
    template_name = 'websites/create_website.html'
