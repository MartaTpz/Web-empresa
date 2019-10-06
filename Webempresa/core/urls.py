from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    #paths del core
    path('', views.home, name="home"),
    path('som/', views.som, name="som"),
    path('història/', views.història, name="història"),
    path('galeria/', views.galeria, name="galeria"),
    path('amics/', views.amics, name="amics"),
    path('export/', views.export, name="export"),
    path('blog/', views.blog, name="blog"),
  
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)