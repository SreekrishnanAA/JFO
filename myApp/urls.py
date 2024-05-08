from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("organize", views.organize), 
    path("statistics", views.statistics),
    path("login", views.login),
    path("logout", views.logout),
    path("about", views.about),

]
