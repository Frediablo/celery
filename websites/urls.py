from django.urls import path
from .views import *

urlpatterns = [
    path('', WebsiteListView.as_view(), name='websites'),
    path('website/<int:id>/', WebsiteDetailView.as_view(), name='website-detail-view')
]