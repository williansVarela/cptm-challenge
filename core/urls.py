"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from core.controllers import login, profile, dashboard

urlpatterns = [
    path('api/', include('api.urls'), name='api'),
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('login/', login.LoginView.as_view(), name='login'),
    path('', dashboard.HomeView.as_view(), name='home'),

    path('account/profile/', profile.UpdateProfileView.as_view(), name='profile'),
    path('account/password/', profile.PasswordResetByUser.as_view(), name='change_password'),

    path('dashboard/<str:line>/', dashboard.DashboardView.as_view(), name='dashboard'),
]
