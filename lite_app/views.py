from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context_dict = {'boldmessage': 'Hi there!'}
    return render(request, 'lite_app/index.html', context_dict)
