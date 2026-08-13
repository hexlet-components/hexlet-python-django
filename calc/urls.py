from django.urls import path
from calc import views

app_name = 'calc'
urlpatterns = [
    path('<int:a>/<int:b>', views.IndexView.as_view(), name='index'),
    path('history', views.HistoryView.as_view(), name='history'),
]
