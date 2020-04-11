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
from django.urls import path
from django.views.generic import TemplateView

from user_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('userpage/', TemplateView.as_view(template_name="user_temp/user_login.html"),name="userpage"),
    path('save_reg_details/',views.saveregdetails,name="save_reg_details"),
    path('user_home/',views.userhomepage,name="user_home"),
    path('home/',views.user_home,name="home"),
    path('home/', TemplateView.as_view(template_name="user_temp/user_home.html"), name="home"),
    # path('apply/',TemplateView.as_view(template_name="user_temp/user_leave.html"),name="apply_leave")
    path('apply/',views.applyleave,name="apply_leave"),
    path('save_leave/',views.saveleave,name="save_leave"),
    path('logout/', TemplateView.as_view(template_name="user_temp/user_login.html"), name="logout"),
    path('notify/',views.notification,name='notify')

]
