from django.shortcuts import render, redirect
from .models import Complains,Daily_Usage
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.db.models import Sum
import json,requests
from MyApp.models import Pricing

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
    phone_number = request.POST.get('PhoneNumber', request.GET.get('PhoneNumber'))
    thirty_days_ago = datetime.now() - timedelta(days=30)
    user_usage = Daily_Usage.objects.filter(phonenumber=phone_number, date__gte=thirty_days_ago)
    total_local_sms = user_usage.aggregate(total_LocalSMSPricing=Sum('LocalSMSPricing'))['total_LocalSMSPricing']
    total_gprs = user_usage.aggregate(total_GPRSPricing=Sum('GPRSPricing'))['total_GPRSPricing']
    total_offnet_calls = user_usage.aggregate(total_OffNetPricing=Sum('OffNetPricing'))['total_OffNetPricing']
    total_onnet_calls = user_usage.aggregate(total_OnNetPricing=Sum('OnNetPricing'))['total_OnNetPricing']
    total_irish_landline = user_usage.aggregate(total_IrishLandlinePricing=Sum('IrishLandlinePricing'))['total_IrishLandlinePricing']
    total_international_call = user_usage.aggregate(total_InternationalCallPricing=Sum('InternationalCallPricing'))['total_InternationalCallPricing']
    total_international_sms = user_usage.aggregate(total_InternationalSMSPricing=Sum('InternationalSMSPricing'))['total_InternationalSMSPricing']
    user_usage={
        'Local SMS': total_local_sms,
        'GPRS': total_gprs,
        'Off Net Calls': total_offnet_calls,
        'On Net Calls': total_onnet_calls,
        'Irish Landline Calls': total_irish_landline,
        'International Calls': total_international_call,
        'International SMSs': total_international_sms }
    pricing_instance = Pricing.objects.filter().first()
    pricing_map = {}
    api_trigger_data = []
    if pricing_instance:
        pricing_map = {
    'Local SMS': pricing_instance.LocalSMSPricing,
    'GPRS': pricing_instance.GPRSPricing,
    'Off Net Calls': pricing_instance.OffNetPricing,
    'On Net Calls': pricing_instance.OnNetPricing,
    'Irish Landline Calls': pricing_instance.IrishLandlinePricing,
    'International Calls': pricing_instance.InternationalCallPricing,
    'International SMSs': pricing_instance.InternationalSMSPricing,}
    if request.method == 'POST':
        emailid = request.POST.get('emailid')
        for item, amount in user_usage.items():
            price = pricing_map[item]
            api_trigger_data.append({"item": item, "amount": str(amount), "price": str(price)})
        payload = {
        "emailid": emailid,
        "data": api_trigger_data}
        api_url = 'https://9w9hrve1k6.execute-api.us-east-1.amazonaws.com/PDFGen/products'
        response = requests.post(api_url, json=payload)
        if response.status_code == 200:
            return render(request,'index.html')
        else:
            return render(request,'index.html')
    return render(request, 'Usage_resutls.html',{'user_usage': user_usage})
    
def Weekly_Usage(request):
    return render(request, 'Weekly_Usage.html')

def Weekly_Usage_results(request):
    if request.method == 'POST':
        phone_number = request.POST.get('user_number')
        start_date = request.POST.get('Start')
        end_date = request.POST.get('End')
        
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        
        usage_records = Daily_Usage.objects.filter(date__range=[start_date, end_date], phonenumber=phone_number)
        
        data_to_send = {
         "data": [
            {"amount": int(round(float(record.GPRSPricing))), "date": record.date.strftime("%Y-%m-%d")}
             for record in usage_records] }
        api_url = 'https://746x7jtblf.execute-api.us-east-1.amazonaws.com/dev/analyze'
        
        try:
            response = requests.post(api_url, json=data_to_send)
            response_data = response.json()
            
            if response.status_code == 200:
                return render(request, 'Weekly_Usage_results.html', {'api_response': response_data, 'usage_records': usage_records})
            else:
                return HttpResponse(f"API call failed with status code {response.status_code}", status=500)
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"API call error: {str(e)}", status=500)
    else:
        return render(request, 'Weekly_Usage_results.html')