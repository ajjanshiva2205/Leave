from django.shortcuts import render,redirect
from user_app.models import RegistrationModel
from admin_app.models import ApplyLeaveModel
from django.contrib import messages



# Create your views here.
def saveregdetails(request):
    r1 = request.POST['r1']
    r2 = request.POST['r2']
    r3 = request.POST['r3']
    r4 = request.POST['r4']
    r5 = request.POST['r5']
    r6 = request.POST['r6']
    r7 = request.POST['r7']
    status = "pending"
    RegistrationModel(idno=r1,name=r2,email=r3,contact=r4,password=r5,dept=r6,status=status,designation=r7).save()
    messages.success(request,"Saved Successfully...! Admin Need Approve")
    return redirect("userpage")


def userhomepage(request):
    id = request.POST['l1']
    pwd = request.POST['l2']
    option = request.POST['l3']
    print(id,pwd,option)
    qs = RegistrationModel.objects.filter(idno=id, password=pwd, designation=option)
    if qs:
        request.session['id'] = id
        return render(request,"user_temp/user_home.html",{"data":qs})
    else:
        messages.error(request,"Sorry...! Invalid Dxetails")
        return redirect('userpage')

def     user_home(request):
    return redirect("home")

def applyleave(request):
    id=request.session["id"]
    id=RegistrationModel.objects.get(idno=id)
    return render(request, "user_temp/user_leave.html", {"data":id})


def saveleave(request):
    id = request.POST.get("a1")
    des = request.POST.get("a2")
    to = request.POST.get("a3")
    dept = request.POST.get("a4")
    type = request.POST.get("a5")
    s_dt = request.POST.get("a6")
    l_dt = request.POST.get("a7")
    r = request.POST.get("a8")
    status = "pending"
    print(id,des,to,dept,type,s_dt,l_dt,r)
    ApplyLeaveModel(idno=id,des=des,gamil=to,dept=dept,l_type=type,s_date=s_dt,l_date=l_dt,reason=r,status=status).save()
    messages.success(request,"leave apply is success. Need to approve")
    return redirect('apply_leave')


def notification(request):
    id=request.session['id']
