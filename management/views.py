from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def management(request):
    
     if not request.user.is_staff:
          return redirect("home")
     
     return render(request, "management/management.html")
