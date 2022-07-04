from django.urls import path

from hello_django.calc import views

urlpatterns = [
    path('', views.index),
]
