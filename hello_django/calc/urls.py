from django.urls import path
from hello_django.calc.views import CalcPageView

urlpatterns = [
    path('', CalcPageView.as_view()),
]
