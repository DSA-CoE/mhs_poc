"""mhs_poc URL Configuration

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
from django.urls import include, path

from mhs_poc.config.settings import ADMIN_URL

urlpatterns = [
    path(
        "admin/", include("admin_honeypot.urls", namespace="admin_honeypot")
    ),  # Honeypot
    path("{}/".format(ADMIN_URL), admin.site.urls),
    path("microsoft/", include("microsoft_auth.urls", namespace="microsoft")),
    path("", include("mhs_poc.apps.auth_azure_ad.urls")),
    path("", include("mhs_poc.apps.base.urls")),
]
