from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MainForm
from .models import User
from django.shortcuts import redirect
 

def index(request):
    # def get(self, request):
    #     form = MainForm()
    #     return render(request, 'main/index.html', context={'form': form})

    # def post(self, request):
    #     print()
    #     print(dir(request))
    #     print()
    #     print(request.POST)
    #     bound_form = MainForm()
    
    if request.method == 'POST':
        form = MainForm(request.POST)
        # if form.is_valid():
        form.save()
        print(form.cleaned_data)
        return redirect("/main")
    
    else:
        form = MainForm()
    return (render(request, 'main/index.html', {'form': form}))


def main(request):
    return render(request, 'main/main.html')

def about_us(request):
    return render(request, 'main/about_us.html')

def someview(request):
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))