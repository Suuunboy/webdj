from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'main/index.html')

def main(request):
    return render(request, 'main/main.html')

def about_us(request):
    return render(request, 'main/about_us.html')

def someview(request):
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))