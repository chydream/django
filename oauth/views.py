from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("oauth index")

class ShowClassView(TemplateView):
    template_name = 'show_class.html'

def show_filter(request):
    return render(request, 'show_filter.html', {
        'name': '这是测试'
    })