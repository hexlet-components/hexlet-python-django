from django.urls import path
from hello_django.calc.views import index, history

urlpatterns = [
    path('<int:a>/<int:b>', index.as_view(), name='calc'),
    path('history', history.as_view())
]
