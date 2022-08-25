from django.urls import path
from hello_django.calc import views

app_name = 'calc'
urlpatterns = [
    path('', views.index, name='index'),
]
