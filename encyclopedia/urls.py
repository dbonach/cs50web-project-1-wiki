from django.urls import path, re_path

from . import views

app_name = 'encyclo'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/", views.wiki, name="entry"),
    path("new", views.newPage, name="newpage"),
    path("edit/<str:entry>/", views.edit, name="edit"),
    path("random", views.randomPage, name="randomPage")
]
