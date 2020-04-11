from django.shortcuts import render,redirect
from django.contrib import messages
from user_app.models import RegistrationModel
from django.db.models import Q

def check_login(request):
    idno = request.POST.get("a1")
    pwd = request.POST.get("a2")
    print(idno,pwd)
    if idno == "admin" and pwd == "admin":
        return redirect("admin_home")
    else:
        messages.error(request,"Invalid Details")
        return redirect("admin_page")

def userRequest(request):
    qs = RegistrationModel.objects.filter(status='pending')
    return render(request,"admin_temp/userrequest.html",{"data":qs})


def declineRequest(request):
    idno = request.POST.get("h2")
    print(idno)
    qs = RegistrationModel.objects.filter(idno=idno)
    qs.update(status="request_declined")
    messages.success(request,"request_declined")
    return redirect('user_req')

def approve(request):
    id = request.POST.get("h1")
    print(id)
    qs = RegistrationModel.objects.filter(idno=id)
    qs.update(status="request_approved")
    messages.success(request,"approved successfully")
    return redirect('user_req')


def decline(request):
    qs = RegistrationModel.objects.filter(status="request_declined")
    return render(request,"admin_temp/decline_req.html",{"data":qs})