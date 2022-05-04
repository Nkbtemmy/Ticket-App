from django.contrib import admin
from django.urls import path,include
from APIs.Views import Event

urlpatterns = [
    path("", Event.default, name="default Event Route"),
    path("new", Event.createEvent, name="create Event Route"),
    path("all", Event.viewEvents, name="View all Events Route"),
    path("<str:id>", Event.viewEvent, name="create Event Route"),
]