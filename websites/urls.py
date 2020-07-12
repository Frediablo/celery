from django.urls import path
from .views import *

urlpatterns = [
    path('', WebsiteListView.as_view(), name='websites'),
    path('create-website/', CreateWebsite.as_view(), name='create-website'),
    path('website/<int:id>/', WebsiteDetailView.as_view(), name='website-detail-view')
]