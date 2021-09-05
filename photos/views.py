from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse, Http404
import datetime as dt
from .models import Image,Category,Location

# Create your views here.

def index(request):
    gallery = Image.objects.all()[:6]
    return render(request,'index.html', {'gallery':gallery})


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


def kenya(request):
    kenya_category = Category.objects.get(pk=1)
    kenya = Image.objects.all().filter(category=kenya_category)
    return render(request,'category/kenya/kenya.html', {'kenya':kenya})


def uganda(request):
    uganda_category = Category.objects.get(pk=2)
    uganda = Image.objects.filter(category=uganda_category)
    return render(request,'category/uganda/uganda.html', {'uganda':uganda})


def tanzania(request):
    tanzania_category = Category.objects.get(pk=5)
    tanzania = Image.objects.filter(category=tanzania_category)
    return render(request,'category/tanzania/tanzania.html', {'tanzania':tanzania})

def rwanda(request):
    rwanda_category = Category.objects.get(pk=3)
    rwanda = Image.objects.filter(category=rwanda_category)
    return render(request,'category/rwanda/rwanda.html', {'rwanda':rwanda})

def burundi(request):
    burundi_category = Category.objects.get(pk=3)
    burundi = Image.objects.filter(category=burundi_category)
    return render(request,'category/burundi/burundi.html', {'burundi':burundi})

def somalia(request):
    somalia_category = Category.objects.get(pk=3)
    somalia = Image.objects.filter(category=somalia_category)
    return render(request,'category/somalia/somalia.html', {'somalia':somalia})

def ethiopia(request):
    ethiopia_category = Category.objects.get(pk=3)
    ethiopia = Image.objects.filter(category=ethiopia_category)
    return render(request,'category/ethiopia/ethiopia.html', {'ethiopia':ethiopia})

def sudan(request):
    sudan_category = Category.objects.get(pk=3)
    sudan = Image.objects.filter(category=sudan_category)
    return render(request,'category/sudan/sudan.html', {'sudan':sudan})