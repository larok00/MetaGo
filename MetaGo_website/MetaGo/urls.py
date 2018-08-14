from django.urls import path, re_path

from . import views

app_name="MetaGo"
urlpatterns = [
    path('', views.index, name='index'),
    re_path('^photo_id/$', views.photo_id, name='photo_id'),
]


