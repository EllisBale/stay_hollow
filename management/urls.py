from django.urls import path
from . import views


urlpatterns = [
    path('', views.management, name='management'),
    # User
    path('user_list/', views.user_mangement, name='user_list'),
    path('edit/<int:pk>/', views.user_update, name='user_form'),
    path('delete/<int:pk>/', views.user_delete, name="delete_user"),



    path('listings_list/', views.listing_management, name='listings_list'),
    path('booking_list/', views.booking_management, name='booking_list'),
    path('reviews_list/', views.reviews_management, name='reviews_list'),
]