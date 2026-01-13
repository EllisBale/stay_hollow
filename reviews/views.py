from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bookings.models import Booking
from listings.models import Property

from .forms import ReviewForm


@login_required
def add_review(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    booking = (
        Booking.objects
        .filter(
            user=request.user,
            property=property_obj,
            is_paid=True
        )
        .exclude(review__isnull=False)
        .first()
    )

    if not booking:
        messages.error(request, "You cannot review this property.")
        return redirect("property_detail", pk=property_obj.id)
    
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form .is_valid():
            review = review_form .save(commit=False)
            review.booking = booking
            review.user = request.user
            review.save()
            
            messages.success(request, "Review Submitted!")
            return redirect("property_detail", pk=property_obj.id)
    else:
        review_form = ReviewForm()

    return render(request, "reviews/add_review.html", {
        "review_form": review_form ,
        "property": property_obj,
    })
