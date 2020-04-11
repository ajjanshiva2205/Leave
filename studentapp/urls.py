"""Leave URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from studentapp import views

urlpatterns = [
    path('',TemplateView.as_view(template_name="student_temp/st_login.html"), name="studentpage"),
    path('student_home/',views.student_home,name="student_homepage"),
    path('home_st/', TemplateView.as_view(template_name="student_temp/st_menu.html"), name="home_st"),
    path('logout_st/', TemplateView.as_view(template_name="student_temp/st_login.html"), name="logout_st"),
    path('leave_save/',views.leavesave,name="leave_save"),

    path('apply_leave_st/',views.applyleave_st,name="apply_leave_st"),
    # path('apply_leave_st/',TemplateView.as_view(template_name="student_temp/st_leave.html"),name="apply_leave_st"),
    # path('student_homepage/',TemplateView.as_view(template_name="student_temp/st_menu.html"),name="student_homepage"),
]
