from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Property, Destination
from bookings.models import Booking

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
                selected_destinations = Destination.objects.filter(name__in=destinations_names)

                properties = properties.filter(
                    Q(destinations__name__in=destinations_names) |
                    Q(destinations__parent_destination__name__in=destinations_names)
                )


        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criterial")
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
            properties = properties.order_by("price_per_night")

        elif sortby == "price_desc":
             properties = properties.order_by("-price_per_night")

        elif sortby == "newest":
            properties = properties.order_by("-id")

    paginator = Paginator(properties, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "search_term": query,
        "selected_destinations": selected_destinations,
        "page_obj": page_obj,
    }

    return render(request, "listings/property_list.html", context)


def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)

    has_paid_booking = False

    if request.user.is_authenticated:
        has_paid_booking = Booking.objects.filter(
            user=request.user,
            property=property_obj,
            is_paid=True,

        ).exists()

    context = {
        "property": property_obj,
        "has_paid_booking": has_paid_booking,
    }

    return render(request, "listings/property_detail.html", context)
