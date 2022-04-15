"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from login.views import *
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("logout", logout_request, name="logout"),
    path("logout", logout_request, name= "logout"),
    path("home", homepage, name="home"),
    path("", homepage, name="home"),
    path("place", place, name="place"),
    path("machine", machine, name="machine"),
    path("record", record, name="record"),
    path("status", status, name="status"),
    path("examine", examine, name="examine"),
    path("examine_date", examine_date, name="examine_date"),
    path("examine_date_place", examine_date_place, name="examine_date_place"),
    path("show_date", show_date, name="show_date"),
    path("examine_status", examine_status, name="examine_status"),
    path("show_status", show_status, name="show_status"),
]

handler404 = view_404