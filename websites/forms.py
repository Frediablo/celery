from .models import Website
from django.forms import ModelForm


class WebsiteModelForm(ModelForm):
    class Meta:
        model = Website
        fields = '__all__'
