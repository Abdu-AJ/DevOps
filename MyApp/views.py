from django.shortcuts import render, redirect
from .models import Complains
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Complains
# Create your views here.
def index(request):
    return render(request,'index.html')
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
def Tracking(request):
    return render(request, 'Tracking.html')
    
def Result(request):
    phone_number = request.GET.get('PhoneNumber')
    complaints = Complains.objects.filter(phonenumber=phone_number) if phone_number else None
    return render(request, 'searchresult.html', {'complaints': complaints})