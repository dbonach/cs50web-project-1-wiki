from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("wiki/CSS", views.wiki, name="css")
    # path("<char:title>", views.wiki, name="css")
    re_path(r'^wiki/(\w+)/$', views.wiki, name='entry')

]
