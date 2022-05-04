from django.contrib import admin
from django.urls import path,include
from APIs.Views import Role

urlpatterns = [
    path("", Role.default, name="default Role Route"),
    path("new", Role.saveRoles, name="create Role Route"),
    path("all", Role.getRoles, name="get Roles Route"),
]