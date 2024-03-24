from django.shortcuts import render, redirect
from .models import Complains,Usage
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import json
import requests

def index(request):
    return render(request,'index.html')
@login_required    
@csrf_exempt
def NewTicket(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        phonenumber = request.POST.get('PhNum')
        complain = request.POST.get('Description')
        comments = 'To be Updated'
        complain = Complains(email=email, phonenumber=phonenumber, complain=complain, comments=comments)
        complain.save()
        return redirect('index')
    return render(request,'NewTicket.html')
@login_required    
def Tracking(request):
    return render(request, 'Tracking.html')
    
def Result(request):
    phone_number = request.GET.get('PhoneNumber')
    complaints = Complains.objects.filter(phonenumber=phone_number) if phone_number else None
    return render(request, 'searchresult.html', {'complaints': complaints})

@login_required     
def User_Usage(request):
    return render(request, 'Usage.html')
    
def Usage_results(request):
    phone_number = request.GET.get('PhoneNumber')
    user_usage = Usage.objects.filter(phonenumber=phone_number) if phone_number else None
    return render(request, 'Usage_resutls.html', {'user_usage': user_usage})