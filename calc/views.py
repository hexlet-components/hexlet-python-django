from django.shortcuts import render
from django.views import View

from .models import History


class IndexView(View):

    def get(self, request, a, b):
        sum_ = a + b
        History(value=sum_).save()
        return render(
            request,
            'calc/index.html',
            {'a': a, 'b': b, 'sum': sum_},
        )


class HistoryView(View):

    def get(self, request):
        calc_history = History.objects.order_by('-timestamp')[:10]
        return render(request, 'calc/history.html', {'history': calc_history})
