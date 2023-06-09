from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from .models import Post, Like
from django.contrib.auth.models import User
from django.http import JsonResponse
 

# def index(request):
    
#     if request.method == 'POST':
#         email = request.POST['email']
#         form = MainForm(request.POST)
#         if validateEmail(email):
#             form.save()
#             print(form.cleaned_data)
#             return redirect("/main")
    
#     else:
#         form = MainForm()
#     return (render(request, 'main/index.html', {'form': form}))

def index(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created: ', form.cleaned_data.get('username'))
            return redirect('/login')

    return (render(request, 'main/index.html', {'form': form}))

def validateEmail( email ):


    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False


def main(request):
    return render(request, 'main/main.html')

def about_us(request):
    return render(request, 'main/about_us.html')

def profile(request):
    user = request.user
    return render(request, 'main/profile.html', {'user': user})

def someview(request):
   return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return redirect('/main')
    return render(request, 'main/login.html')

def new_post(request):
    qs = Post.objects.all()
    user = request.user
    context = {
        'qs': qs,
        'user': user,
    }

    return render(request, 'main/post.html', context)

def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        
        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'

            else:
                like.value='Like'
        else:
            like.value='Like'

            post_obj.save()
            like.save()

        data = {
            'value': like.value,
            'likes': post_obj.likes.all().count()
        }
        # return JsonResponse(data, safe=False)

    return redirect('/main/post')