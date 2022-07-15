from django.views.generic.base import TemplateView
from django.shortcuts import redirect

class IndexView(TemplateView):
    def get(self, request):
        return redirect('calc', a='40', b='2')

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context
