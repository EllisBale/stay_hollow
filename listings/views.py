from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Property, Destination
from bookings.models import Booking
from reviews.models import Review


def property_list(request):
    """
    Renders properties list.
    """

    properties = Property.objects.all()
    query = None
    selected_destinations = None

    if request.GET:

        if "destinations" in request.GET:

            destinations_param = request.GET.get("destinations")
            if destinations_param:
                destinations_names = destinations_param.split(",")
                selected_destinations = Destination.objects.filter(
                    name__in=destinations_names
                )

                is_dest = Q(destinations__name__in=destinations_names)
                is_parent = Q(
                    destinations__parent_destination__name__in=destinations_names  # noqa
                )
                properties = properties.filter(is_dest | is_parent).distinct()

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criterial"
                )

                return redirect(reverse('properties'))

            queries = (
                Q(property_name__icontains=query) |
                Q(bedrooms__icontains=query) |
                Q(guests__icontains=query) |
                Q(description__icontains=query) |
                Q(destinations__name__icontains=query) |
                Q(destinations__parent_destination__name__icontains=query)
            )

            properties = properties.filter(queries)

        sortby = request.GET.get("sort")

        if sortby == "price_asc":
            properties = properties.order_by(
                "price_per_night"
            )

        elif sortby == "price_desc":
            properties = properties.order_by(
                "-price_per_night"
            )

        elif sortby == "newest":
            properties = properties.order_by("-id")

    paginator = Paginator(properties, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    property_total = properties.count()

    context = {
        "search_term": query,
        "selected_destinations": selected_destinations,
        "page_obj": page_obj,
        "property_total": property_total,
    }

    return render(request, "listings/property_list.html", context)


def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)

    has_paid_booking = False
    has_reviewed = False

    if request.user.is_authenticated:
        has_paid_booking = Booking.objects.filter(
            user=request.user,
            property=property_obj,
            is_paid=True,

        ).exists()

        has_reviewed = Review.objects.filter(
            booking__user=request.user,
            booking__property=property_obj

        ).exists()

    reviews = Review.objects.filter(
        booking__property=property_obj
    )

    reviews_preview = reviews[:3]

    context = {
        "property": property_obj,
        "has_paid_booking": has_paid_booking,
        "has_reviewed": has_reviewed,
        "reviews": reviews,
        "reviews_preview": reviews_preview,
    }

    return render(request, "listings/property_detail.html", context)
