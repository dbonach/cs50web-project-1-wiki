from django.urls import path, re_path

from . import views

app_name = 'encyclo'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/", views.wiki, name="entry")
    # re_path(r'^wiki/(\w+)/$', views.wiki, name='entry')
]
