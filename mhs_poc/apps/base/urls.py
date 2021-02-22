from django.urls import path

from mhs_poc.apps.base import views

urlpatterns = [
    path("", views.home_view),
    path("home", views.home_view, name="home"),
    path("profile", views.profile_view, name="profile"),
]
