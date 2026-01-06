from django.shortcuts import render
from listings.models import Property


def index(request):
    """ Returns the index page """
    
    featured_properties = Property.objects.filter(is_featured=True)

    return render(request, "home/index.html", {"featured_properties": featured_properties})


def about(request):
    """ Returns the about page"""

    return render(request, "home/about.html",)


def contact(request):
    """ Returns the contact page"""

    return render(request, "home/contact.html",)