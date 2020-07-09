from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.


class WebsiteListView(ListView):
    queryset = Website.objects.all().order_by('id')
    template_name = 'websites/websites.html'
    paginate_by = 100


class WebsiteDetailView(DetailView):
    pass


class CreateWebsite(CreateView):
    pass
