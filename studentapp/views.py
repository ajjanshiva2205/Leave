from django.shortcuts import render,redirect
from django.contrib import messages
from user_app.models import RegistrationModel
from admin_app.models import ApplyLeaveModel


def student_home(request):
    l1 = request.POST['l1']
    l2 = request.POST['l2']
    l3 =request.POST['l3']
    try:
        # id=request.session['id']
        RegistrationModel.objects.get(idno=l1,password=l2,designation=l3)
    except:
        messages.success(request,"Sorry...! Invalid Login Details")
        return redirect('studentpage')
    else:
        return render(request, "student_temp/st_menu.html",{"data":"Welcome To Student HomePage"})

def applyleave_st(request):
    id = request.session["id"]
    qs = RegistrationModel.objects.get(idno=id)
    return render(request,"student_temp/st_leave.html",{"data1":qs})

def leavesave(request):
    id = request.POST.get("a1")
    des = request.POST.get("a2")
    to = request.POST.get("a3")
    dept = request.POST.get("a4")
    type = request.POST.get("a5")
    s_dt = request.POST.get("a6")
    l_dt = request.POST.get("a7")
    r = request.POST.get("a8")
    status = "pending"
    print(id,des,to, dept,type,s_dt,l_dt,r)
    ApplyLeaveModel(idno=id,des=des,gamil=to,dept=dept,l_type=type,s_date=s_dt,l_date=l_dt,reason=r,status=status).save()
    messages.success(request,"leave apply is success.Need to approve")
    return redirect('leave_save')