from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Models
from listings.models import Property, PropertyImage
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

     paginator = Paginator(users, 10)
     page_number = request.GET.get("page")
     page_obj = paginator.get_page(page_number)

     context = {
          "users" : users,
          "page_obj" : page_obj,
     }

     return render(request, "management/user_list.html", context)


@login_required
def user_update(request, pk):
     """
     Update User
     """
     if not request.user.is_staff:
          return redirect("home")
     
     user = get_object_or_404(User, pk=pk)


     if user.is_superuser and not request.user.is_superuser:
          return redirect("user_list")

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

     if user.is_superuser and not request.user.is_superuser:
          return redirect("home")

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

     paginator = Paginator(listings, 10)
     page_number = request.GET.get("page")
     page_obj = paginator.get_page(page_number)

     context = {
          "listings" : listings,
          "page_obj" : page_obj,

     }

     return render(request, "management/listings_list.html", context)


@login_required
def listing_update(request, pk):
     """
     Update Listing
     """
     if not request.user.is_staff:
          return redirect("home")
     
     listing = get_object_or_404(Property, pk=pk)

     if request.method == "POST":
          listing_form = ListingForm(request.POST, request.FILES, instance=listing)

          images_form = ImagesForm(request.POST, request.FILES)

          if listing_form.is_valid() and images_form.is_valid():

               listing_form.save()

               image = images_form.save(commit=False)
               image.property = listing
               image.save()


               messages.success(request, "Property Updated Successfully")
               return redirect("listings_list")
     else:
          listing_form = ListingForm(instance=listing)
          images_form = ImagesForm()
          
     return render(request, "management/listing_form.html", {
          "listing_form" : listing_form,
          "images_form": images_form,
          "listing" : listing,
          "property_images": listing.extra_images.all(),
     })



@login_required
def listing_delete(request, pk):
     """
     Delete User Booking
     """
     if not request.user.is_staff:
          return redirect("home")

     listing = get_object_or_404(listing, pk=pk)
     listing.delete()
     messages.success(request, "Listing Deleted Successfully")
     return redirect("listings_list")



@login_required
def delete_property_image(request, pk, image_id):
     """
     Delete A Property Image
     """
     if not request.user.is_staff:
          return redirect("home")

     image = get_object_or_404(PropertyImage, pk=image_id)

     if image.property.pk != pk:
          return messages.error("You are not authorised to delete this image.")
     
     image.delete()

     messages.success(request, "Image deleted successfully.")
     return redirect("edit_listing", pk=pk)


# ----------------------------
#   Booking Management (CRUD)
# ----------------------------
@login_required
def booking_management(request):
     if not request.user.is_staff:
          return redirect("home")
     
     bookings = Booking.objects.filter(is_paid = True)

     paginator = Paginator(bookings, 10)
     page_number = request.GET.get("page")
     page_obj = paginator.get_page(page_number)


     context = {
          "bookings" : bookings,
          "page_obj": page_obj,
     }

     return render(request, "management/booking_list.html", context)


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


     paginator = Paginator(reviews, 10)
     page_number = request.GET.get("page")
     page_obj = paginator.get_page(page_number)

     context = {
          "reviews" : reviews,
          "page_obj" : page_obj,

     }

     return render(request, "management/reviews_list.html", context)


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
