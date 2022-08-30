from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request, a, b):
        sum_ = a + b
        return render(
            request,
            'calc/index.html',
            {'a': a, 'b': b, 'sum': sum_},
        )
