from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index, name = 'home'),
    url(r'^gallery/$', views.gallery, name = 'gallery'),
    url(r'^gallery/<int:image_id>/$', views.single_image_details, name='details'),
    url(r'^search/', views.search_category, name = 'search_category'),
    url(r'^category/kenya/$', views.kenya, name = 'kenya'),
    url(r'^category/tanzania/$', views.tanzania, name = 'tanzania'),
    url(r'^category/uganda/$', views.uganda, name = 'uganda'),
    url(r'^category/rwanda/$', views.rwanda, name = 'rwanda'),
    url(r'^category/burundi/$', views.burundi, name = 'burundi'),
    url(r'^category/somalia/$', views.somalia, name = 'somalia'),
    url(r'^category/ethiopia/$', views.ethiopia, name = 'ethiopia'),
    url(r'^category/sudan/$', views.sudan, name = 'sudan'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)