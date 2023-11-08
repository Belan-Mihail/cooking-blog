from django.shortcuts import render
from django.core.exceptions import PermissionDenied


def handler404(request, exception):
    """Function to render 404.html if error appears."""
    return render(request, '404.html', status=404)


def handler500(request):
    """Function to render 500.html if error appears."""
    return render(request, '500.html', status=500)