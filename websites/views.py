from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.


class WebsiteListView(ListView):
    pass


class WebsiteDetailView(DetailView):
    pass


class CreateWebsite(CreateView):
    pass
