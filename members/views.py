from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def login_user(request):
    if request.method== "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,"There Was An Error Loging In Try Again")
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('index')