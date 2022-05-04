from django.contrib import admin
from django.urls import path,include
from APIs.Views import Tickets

urlpatterns = [
    path("", Tickets.default, name="default Tickets Route"),
    path("new", Tickets.saveTicket, name="create Ticket Route"),
    path("all", Tickets.getTickets, name="get Ticket Route"),
]