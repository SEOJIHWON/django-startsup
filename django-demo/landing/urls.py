from django.urls import path

from landing import views

app_name = "landing"

urlpatterns = [

    path("",views.index) ,
    path("create/",views.post_create, name="create"),
    path("read-all/",views.post_read_all, name="read-all"),
    path("read/<int:post_id>/", views.post_read, name="read"), #path variable
    path("update/<int:post_id>/", views.post_update , name="update"),
    path("delete/<int:post_id>/", views.post_delete, name="delete") ,
    path("temptest/", views.temptest),
    path("path-test/<int:i>/<int:j>/", views.temptest, name="url_test"),

]