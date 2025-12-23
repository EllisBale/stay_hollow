from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from listings.models import Property
from bookings.models import Booking
from reviews.models import Review


@login_required
def management(request):
    
     if not request.user.is_staff:
          return redirect("home")
     
     total_properties = Property.objects.count()

     total_users = User.objects.count()

     total_bookings = Booking.objects.filter(is_paid=True).count()

     total_reviews = Review.objects.count()

     context = {
          "total_properties" : total_properties,
          "total_users" : total_users,
          "total_bookings" : total_bookings,
          "total_reviews" : total_reviews,
     }

     return render(request, "management/management.html", context)
