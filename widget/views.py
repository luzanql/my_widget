from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'message': 'hola'}
    return render(request, 'widget/index.html', context)
# Create your views here.
