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
    images = Image.get_images()
    location = Location.get_location()
    locations = Location.get_location()
    gallery = Image.objects.all()[:6]
    return render(request,'index.html', {'gallery':gallery, 'date':date, 'location':location, 'locations':locations, 'images':images})


def gallery(request):
    gallery = Image.objects.all()
    return render(request, 'gallery/gallery.html', {'gallery':gallery})


def single_image_details(request,image_id):
    image_detail = get_object_or_404(Image, pk=image_id)
    return render(request,'gallery/details.html', {'image_detail':image_detail})


def search_category(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term  =  request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message  = f"{search_term}"
        
        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please provide a valid search query."
        
        return render(request, 'search.html', {"message":message})


def get_image(request, id):
        locations = Location.get_location()
        try:
            image = Image.objects.get(pk = id)
            print(image)
            
        except ObjectDoesNotExist:
            raise Http404()
        
        return render(request, "image.html", {"image":image, "locations":locations})


def urban(request):
    urban_category = Category.objects.get(pk=1)
    urban = Image.objects.all().filter(category=urban_category)
    return render(request,'category/urban/urban.html', {"urban":urban})


def location(request, location):
    images = Image.search_by_location(location)
    locations = Location.get_location()
    message = f"{location}"
    return render(request, 'locations.html', {"message":message, "images":images, "locations":locations})


def category(request, category):
    images = Image.get_by_category(category)
    locations = Location.get_location()
    message = f"{category}"
    return render(request, 'category.html', {"message":message, "images":images, "locations":locations})



def wild(request):
    wild_category = Category.objects.get(pk=1)
    wild = Image.objects.filter(category=wild_category)
    return render(request,'category/wild/wild.html', {'wild':wild})


def traditional(request):
    traditional_category = Category.objects.get(pk=1)
    traditional = Image.objects.filter(category=traditional_category)
    return render(request,'category/traditional/traditional.html', {'traditional':traditional})

def scenic(request):
    scenic_category = Category.objects.get(pk=1)
    scenic = Image.objects.filter(category=scenic_category)
    return render(request,'category/scenic/scenic.html', {'scenic':scenic})