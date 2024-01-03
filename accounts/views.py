from django.shortcuts import render, redirect
from .models import CustomerAccount
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = CustomerAccount.objects.create_user(cd["username"], cd["email"], cd["password"])
            user.first_name = cd["first_name"]
            user.last_name = cd["last_name"]
            user.save()
            messages.success(request, "Registered Successfully", 'success')
            return redirect("accounts:user_login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form" : form})

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd["username"], password = cd["password"])
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully", 'success')
                return redirect("store:home")
            else:
                messages.error(request, "Phone Number or Password is wrong", 'danger')
                return redirect("accounts:user_login")
    else:
        form = UserLoginForm()
    return render(request, "accounts/login.html", {"form" : form})

@login_required(login_url="accounts:user_login")
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out Successfully", 'success')
    return redirect("store:home")