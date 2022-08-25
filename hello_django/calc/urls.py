from django.urls import path
from hello_django.calc import views

urlpatterns = [
    path('<int:a>/<int:b>', views.IndexView.as_view(), name='calc'),
]
