from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

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
    
def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.info(request, "Registration Successful!")
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register_user.html', {'form': form})