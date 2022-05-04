from django.contrib import admin
from django.urls import path,include
from APIs.Views import Transaction

urlpatterns = [
    path("", Transaction.default, name="default Transaction Route"),
    path("new", Transaction.saveTransaction, name="create Role Route"),
    path("all", Transaction.getTransactions, name="create Role Route"),
]