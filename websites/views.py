from django.shortcuts import render, get_object_or_404
from .models import Website
from django.views.generic import ListView, DetailView, CreateView
from .forms import WebsiteModelForm


# Create your views here.
class WebsiteListView(ListView):
    model = Website
    template_name = 'websites/websites.html'


class WebsiteDetailView(DetailView):
    template_name = 'websites/website_detail_view.html'

    def get_context_data(self, **kwargs):
        ctx = super(WebsiteDetailView, self).get_context_data()
        id_ = self.kwargs.get('id')
        website = get_object_or_404(Website, id=id_)
        webpages = website.webpage_set.all().order_by('entity_name')
        ctx['webpages'] = webpages
        return ctx

    def get_object(self, queryset=None):
        website_id = self.kwargs.get('id')
        return get_object_or_404(Website, id=website_id)


class CreateWebsite(CreateView):
    form_class = WebsiteModelForm
    template_name = 'websites/create_website.html'
