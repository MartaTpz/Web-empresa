from django.urls import path
from . import views

urlpatterns = [
    #paths del core
 
    path('blog/', views.blog, name="blog"),
  
]