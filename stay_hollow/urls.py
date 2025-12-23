from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('listings/', include('listings.urls')),
    path('bookings/', include("bookings.urls")),
    path('checkout/', include('checkout.urls')),
    path('reviews/', include('reviews.urls')),
    path('user_account/', include('user_account.urls')),
    path('management/', include('management.urls')),
]
