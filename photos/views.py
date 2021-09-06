from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.templatetags.static import static
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Image,Category,Location
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    date = dt.date.today()
    images = Image.objects.all()
    locations = Location.get_locations()
    gallery = Image.objects.all()[:6]
    print(locations)
    return render(request,'index.html', {'images': images[::-1], 'locations': locations, 'date': date, 'gallery': gallery})


def gallery(request):
    gallery = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'gallery':gallery})


def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'location.html', {'location_images': images})


def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)

        return render(request, 'search_results.html', {"message": message, "images": searched_images})

    else:
        message = "Please enter a valid search query."

        return render(request, 'search_results.html', {"message": message})