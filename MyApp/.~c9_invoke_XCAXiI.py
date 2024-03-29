from django.shortcuts import render, redirect
from .models import Complains,Daily_Usage
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.db.models import Sum

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
    if phone_number:
        thirty_days_ago = datetime.now() - timedelta(days=30)
        
        user_usage = Daily_Usage.objects.filter(phonenumber=phone_number, date__gte=thirty_days_ago)
        
        total_local_sms = user_usage.aggregate(total_LocalSMSPricing=Sum('LocalSMSPricing'))['total_LocalSMSPricing']
        total_gprs = user_usage.aggregate(total_GPRSPricing=Sum('GPRSPricing'))['total_GPRSPricing']
        total_offnet_calls = user_usage.aggregate(total_OffNetPricing=Sum('OffNetPricing'))['total_OffNetPricing']
        total_onnet_calls = user_usage.aggregate(total_OnNetPricing=Sum('OnNetPricing'))['total_OnNetPricing']
        total_irish_landline = user_usage.aggregate(total_IrishLandlinePricing=Sum('IrishLandlinePricing'))['total_IrishLandlinePricing']
        total_international_call = user_usage.aggregate(total_InternationalCallPricing=Sum('InternationalCallPricing'))['total_InternationalCallPricing']
        total_international_sms = user_usage.aggregate(total_InternationalSMSPricing=Sum('InternationalSMSPricing'))['total_InternationalSMSPricing']
    else:
        total_local_sms = None
        total_gprs = None
        total_offnet_calls = None
        total_onnet_calls = None
        total_irish_landline = None
        total_international_call = None
        total_international_sms = None
    
    user_usage={
        'Local SMS': total_local_sms,
        'GPRS': total_gprs,
        'Off Net Calls': total_offnet_calls,
        'On Net Calls': total_onnet_calls,
        'Irish Landline Calls': total_irish_landline,
        'International Calls': total_international_call,
        'International SMSs': total_international_sms }
    return render(request, 'Usage_resutls.html',{'user_usage': user_usage})
    
def Weekly_Usage(request):
    return render(request, 'Weekly_Usage.html')

def Weekly_Usage_results(request):
    return render(request, 'Tracking.html')