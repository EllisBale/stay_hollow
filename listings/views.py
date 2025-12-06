from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Property


def property_list(request):
    """
    Renders properties list.
    """

    properties = Property.objects.all()
    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criterial")
                return redirect(reverse('properties'))
            
            queries = (
                Q(property_name__icontains=query) | 
                Q(description__icontains=query) |
                Q(destinations__name__icontains=query) |
                Q(destinations__parent_destination__name__icontains=query)
            )

            properties = properties.filter(queries)
            

    context = {
        "properties": properties,
        "search_term": query,
    }

    return render(request, "listings/property_list.html", context)


def property_detail(request, pk):
    property_obj = get_object_or_404(Property, pk=pk)
    return render(request, "listings/property_detail.html", {"property": property_obj})
