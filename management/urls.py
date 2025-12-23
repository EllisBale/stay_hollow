from django.urls import path
from . import views


urlpatterns = [
    path('', views.management, name='management'),
    path('user_list/', views.user_mangement, name='user_list')
]