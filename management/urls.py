from django.urls import path
from . import views


urlpatterns = [
    path('', views.management, name='management'),
    path('user_list/', views.user_mangement, name='user_list'),
    path('listings_list/', views.listing_management, name='listings_list'),
    path('booking_list/', views.booking_management, name='booking_list'),
]