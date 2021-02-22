from django.contrib.auth import views as auth_views
from django.urls import include, path

from mhs_poc.apps.auth_azure_ad import views

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="auth/pages/login.html"),
    ),
    path("", include("django.contrib.auth.urls"), name="user"),
    path("account-expired", views.account_expired_view, name="account_expired"),
]
