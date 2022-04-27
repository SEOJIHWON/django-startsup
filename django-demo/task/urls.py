from django.urls import path

from task import views


urlpatterns = [

    path("",views.index),
    path("page/", views.page),
    path("lorem/", views.lorem),
    path("index/", views.back),
    
]