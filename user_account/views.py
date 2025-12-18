from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by("-date")

    return render(
        request,
        "user_account/order_history.html",
        {"orders": orders}
    )
