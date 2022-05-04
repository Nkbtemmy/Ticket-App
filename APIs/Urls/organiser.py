from django.contrib import admin
from django.urls import path,include
from APIs.Views.Organiser import Controllers

urlpatterns = [
    path("", Controllers.default, name="default Organiser Route"),
    path("signup", Controllers.signup, name="signup new user"),
    path("login", Controllers.login, name="login user"),
    path("all", Controllers.getAllOrganiser, name="get all Organisers Route"),
    path("delete/<str:id>", Controllers.delete, name="delete Organiser Route"),
    path("<str:id>", Controllers.getOneOrganiser, name="get Organiser Route"),
    path("profile", Controllers.organiserProfile, name="user's profile"),
]