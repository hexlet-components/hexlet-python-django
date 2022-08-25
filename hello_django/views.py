from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return redirect(reverse('calc', kwargs={'a': 40, 'b': 2}))
