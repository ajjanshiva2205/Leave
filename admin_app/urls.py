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

from admin_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin_page/', TemplateView.as_view(template_name="admin_temp/adminlogin.html"),name="admin_page"),
    path('check_login/',views.check_login,name="check_login"),
    path('admin_home/', TemplateView.as_view(template_name="admin_temp/adminmenu.html"),name="admin_home"),
    # path('user_req/',TemplateView.as_view(template_name="admin_temp/userrequest.html"),name="user_req"),
    path('user_req/',views.userRequest,name="user_req"),
    path('reports_page/',TemplateView.as_view(template_name="reports_temp/reportspage.html"),name="reports_page"),
    path('decline/',views.declineRequest,name="decline"),
    path('view_user/',views.approve,name="view_user"),
    path('req_decline/',views.decline,name="req_decline"),



]
