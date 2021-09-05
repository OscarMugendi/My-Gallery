from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index, name = 'home'),
    url(r'^gallery/$', views.gallery, name = 'gallery'),
    url(r'^gallery/<int:image_id>/$', views.single_image_details, name='details'),
    url(r'^search/', views.search_category, name = 'search_category'),
    url(r'^category/urban/$', views.kenya, name = 'kenya'),
    url(r'^category/wild/$', views.tanzania, name = 'tanzania'),
    url(r'^category/traditional/$', views.uganda, name = 'uganda'),
    url(r'^category/scenic/$', views.rwanda, name = 'rwanda'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)