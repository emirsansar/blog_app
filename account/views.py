from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login, logout


def login_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html",
                          {"error": "Kullanıcı bulunamadı."})

    return render(request, "account/login.html")


def register_request(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["name"]
        last_name = request.POST["surname"]
        password = request.POST["password"]
        re_password = request.POST["re_password"]

        if password == re_password:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html",
                              {
                                 "error": "Bu kullanıcı adı kullanılıyor.",
                                 "username":username, "email":email,
                                 "first_name":first_name, "last_name":last_name
                               })

            elif User.objects.filter(email=email).exists():
                return render(request, "account/register.html",
                              {
                                 "error": "Bu kullanıcı adı kullanılıyor.",
                                 "username":username, "email":email,
                                 "first_name":first_name, "last_name":last_name
                               })

            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()

                return redirect("login")

        else:
            return render(request, "account/register.html",
                            {
                              "error": "Bu kullanıcı adı kullanılıyor.",
                              "username": username, "email": email,
                              "first_name": first_name, "last_name": last_name
                          })

    return render(request, "account/register.html")


def logout_request(request):
    logout(request)
    return redirect("login")