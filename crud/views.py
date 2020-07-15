from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')
def single(request):
    return render(request, 'single.html')


