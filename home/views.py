from django.shortcuts import render
from listings.models import Property

def index(request):
    """ Returns the index page """

    featured_properties = Property.objects.filter(is_featured=True)

    return render(request, 'home/index.html', {"featured_properties": featured_properties})
