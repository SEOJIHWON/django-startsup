
from django.urls import URLPattern, path

from boot import views

app_name = "boot"
urlpatterns = [

    path("base/", views.test),
    path("blog/", views.blog, name='blog'),
    path("contact/", views.contact, name="contact"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("login/", views.login, name="login"),
    path("sign-up/", views.sign_up, name = "sign_up"),
    path("logout/", views.logout, name="logout" )




]