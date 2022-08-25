from django.urls import include, path
from hello_django import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', include('hello_django.calc.urls')),
]
