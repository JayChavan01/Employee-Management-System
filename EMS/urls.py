"""EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='homepage'),
    path('register/', views.Register_Employee, name='register'),
    path('employees/', views.Employee_Details, name='details'),
    path('update/<int:id>/', views.Update_Record, name='update'),
    path('delete/<int:id>/', views.Delete_Record, name='delete'),
    path('export/', views.Export_Employees, name='export'),
]