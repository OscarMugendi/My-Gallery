from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index, name = 'home'),
    url(r'^gallery/$', views.gallery, name = 'gallery'),
    url(r'^gallery/<int:image_id>/$', views.single_image_details, name='details'),
    url(r'^search/', views.search_category, name = 'search_category'),
    url(r'^image/(\d+)', views.get_image, name='image_results'),
    url(r'^category/urban/$', views.urban, name = 'urban'),
    url(r'^category/wild/$', views.wild, name = 'wild'),
    url(r'^category/traditional/$', views.traditional, name = 'traditional'),
    url(r'^category/scenic/$', views.scenic, name = 'scenic'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)