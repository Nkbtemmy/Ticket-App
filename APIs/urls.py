from django.contrib import admin
from django.urls import path,include
from APIs.Views import views
from .Urls import events, organiser, role, ticket, transaction

urlpatterns = [
    path("",views.default, name = 'default endposint'),
    path("events/", include(events)),
    path("organisers/", include(organiser)),
    path("roles/", include(role)),
    path("tickets/", include(ticket)),
    path("transactions/", include(transaction)),
    # path("api-docs/",schema_view)
]