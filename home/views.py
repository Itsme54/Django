import pyautogui
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from home.models import uploads
import pyautogui as pu


# Create your views here.
def home(request):
    return render(request, 'home/index.html')


def signup(request, self=None):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            pu.alert("email already exist")
            return render(request, 'home/signup.html')
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,
                                            last_name=lastname)
            user.save()
            pu.confirm("user created")
            return redirect('/')
    else:
        return render(request, 'home/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponse('hi')
        else:
            pyautogui.alert("Incorrect username or password")
            return render(request, 'home/login.html')

    else:
        return render(request, 'home/login.html')


def uploads(request):
    p = request.FILES['image']
    d = uploads(pic=p)
    d.save()
    pyautogui.alert("upload done")
    d = uploads.objects.all()
    return render(request, 'home/login.html', {'d': d})


def logout(request):
    return render(request, 'home/index.html')
