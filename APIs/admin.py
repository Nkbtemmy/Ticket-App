from django.contrib import admin
from .models import Payment,Organiser, Event, Ticket

models =[Payment,Organiser, Event, Ticket]
# # Register your models here.
admin.site.register(models)
