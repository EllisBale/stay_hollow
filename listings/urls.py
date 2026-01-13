from django.urls import path
from . import views

urlpatterns = [
    path('', views.property_list, name='properties'),
    path('<int:pk>/', views.property_detail, name='property_detail'),
]
