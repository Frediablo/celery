from django.urls import path
from . import views

urlpatterns = [
    path('websites/', views.WebsiteListView.as_view, name='websites'),
    path('website/<int:id>/', views.WebsiteDetailView.as_view, name='website-detail-view')
]