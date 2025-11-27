from django.urls import path
from . import views
from .webhooks import webhook


from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('<int:booking_id>/', views.checkout, name='checkout'),
    path('checkout_success/<str:order_number>/', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path("webhook/", webhook, name="stripe_webhook"),
]