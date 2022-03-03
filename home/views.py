import pyautogui
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.conf import settings

# from home.form import UpdateUserForm, UpdateProfileForm
from home.models import Profile
import pyautogui as pu


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'home/home.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error("email already exist")
            return render(request, 'home/signup.html')
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname,
                                            last_name=lastname)
            user.save()
            messages.success("Account created successfully")
            return redirect('home/login.html')
    else:
        return render(request, 'home/signup.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home/index.html')
        else:
            # "Incorrect username or password"
            messages.error(request, 'Incorrect credentials')
            return render(request, 'home/login.html')

    else:
        return render(request, 'home/login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    request.session.clear()
    return render(request, 'home/logout.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def reset(request):
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']
        if password1 != password2:
            messages.error("Password  Miss Match")
            return render(request, 'home/reset.html')
        else:
            user = User.objects.get(email=email)
            user.set_password(password2)
            user.save()
            messages.success(request, "Password changed successfully")
            return render(request, 'home/login.html')

    else:
        return render(request, 'home/validate.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def validate_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        # user = auth.authenticate(email=email)
        # email = User.objects.get(email=email)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
            messages.error(request, 'Email is not registered')

        if user is not None:
            # pu.alert(request.POST['email'], 'Email is registered')
            context = {
                "user_email": email
            }
            return render(request, 'home/reset.html', context)
        else:
            # pu.alert(request.POST['email'], 'Email is Not registered')
            return render(request, 'home/validate_user.html')

    else:
        return render(request, 'home/validate_user.html')


@login_required
def profile(request):
    return render(request, 'home/profile.html')


def delete_user_view(request):
    return render(request, 'home/delete_user.html')


def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")


def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie created")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesn't accept cookies")
    return response
