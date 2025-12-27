from django.urls import path
from . import views


urlpatterns = [
    path('', views.management, name='management'),
    # User
    path('user_list/', views.user_mangement, name='user_list'),
    path('edit/<int:pk>/', views.user_update, name='user_form'),
    path('delete/<int:pk>/', views.user_delete, name="delete_user"),



    path('listings_list/', views.listing_management, name='listings_list'),

    # Booking
    path('booking_list/', views.booking_management, name='booking_list'),
    path('booking/edit/<int:pk>/update/', views.booking_update, name='edit_booking'),
    path('booking/delete/<int:pk>/', views.booking_delete, name='delete_booking'),

    path('reviews_list/', views.reviews_management, name='reviews_list'),
    path('review/delete/<int:pk>/', views.reviews_delete, name='delete_review'),
]