from django.urls import include, path
from hello_django import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('calc/', include('hello_django.calc.urls')),
]
