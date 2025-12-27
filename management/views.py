from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Models
from listings.models import Property
from bookings.models import Booking
from reviews.models import Review

#Forms
from .forms import *


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


# ----------------------------
#   User Management (CRUD)
# ----------------------------
@login_required
def user_mangement(request):
     if not request.user.is_staff:
          return redirect("home")
     
     users = User.objects.all()

     return render(request, "management/user_list.html", {"users": users})


@login_required
def user_delete(request, pk):
     """
     Delete User
     """
     if not request.user.is_staff:
          return redirect("home")
     
     user = get_object_or_404(User, pk=pk)
     user.delete()
     messages.success(request, "User Deleted Successfully")
     return redirect("user_list")


@login_required
def user_update(request, pk):
     """
     Update User
     """
     if not request.user.is_staff:
          return redirect("home")
     
     user = get_object_or_404(User, pk=pk)

     if request.method == "POST":
          user_form = UserForm(request.POST, instance=user)
          if user_form.is_valid():
               user_form.save()
               messages.success(request, "User Updated Successfully")
               return redirect("user_list")
     else:
          user_form = UserForm(instance=user)
          
     return render(request, "management/user_form.html", {"user_form" : user_form})

@login_required
@require_POST

def user_delete(request, pk):
     """
     Delete User
     """
     if not request.user.is_staff:
          return redirect("home")
     
     user = get_object_or_404(User, pk=pk)
     user.delete()
     messages.success(request, "User Deleted Successfully")
     return redirect("user_list")

# ----------------------------
#   Listings Management (CRUD)
# ----------------------------
@login_required
def listing_management(request):
     if not request.user.is_staff:
          return redirect("home")
     
     listings = Property.objects.all()

     return render(request, "management/listings_list.html", {"listings" : listings })


# ----------------------------
#   Booking Management (CRUD)
# ----------------------------
@login_required
def booking_management(request):
     if not request.user.is_staff:
          return redirect("home")
     
     bookings = Booking.objects.filter(is_paid = True)

     return render(request, "management/booking_list.html", {"bookings" : bookings})


@login_required
def booking_update(request, pk):
     """
     Update User Booking
     """
     if not request.user.is_staff:
         return redirect("home")
     
     booking = get_object_or_404(Booking, pk=pk)

     if request.method == "POST":
          booking_form = BookingForm(request.POST, instance=booking)
          if booking_form.is_valid():
               booking_form.save()
               messages.success(request, "Booking Updated Successfully")
               return redirect("booking_list")
          
     else:
          booking_form = BookingForm(instance=booking)
     return render(request, "management/booking_form.html", {"booking_form" : booking_form})


@login_required
def booking_delete(request, pk):
     """
     Delete User Booking
     """
     if not request.user.is_staff:
          return redirect("home")

     booking = get_object_or_404(Booking, pk=pk)
     booking.delete()
     messages.success(request, "Booking Deleted Successfully")
     return redirect("booking_list")

# ----------------------------
#   Reviews Management (CRUD)
# ----------------------------
@login_required
def reviews_management(request):
     if not request.user.is_staff:
          return redirect("home")
     
     reviews = Review.objects.all()

     return render(request, "management/reviews_list.html", {"reviews" : reviews})


@login_required
def reviews_delete(request, pk):
     """
     Delete User Reviews
     """
     if not request.user.is_staff:
          return redirect("home")

     review = get_object_or_404(Review, pk=pk)
     review.delete()
     messages.success(request, "Review Deleted Successfully")
     return redirect("reviews_list")
