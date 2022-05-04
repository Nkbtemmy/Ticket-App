from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from APIs.Database.index import Transaction

@api_view(['GET'])
def default(request):
    return Response({"message":"Welcome to Transaction homepage"})

@api_view(['POST'])
def saveTransaction(request):
    try:
        datas = {
            "type":request.data['type'],
            "date_and_time": request.data['data_and_time'],
            "quantity": request.data['quantity']
        }
        results = Transaction.document().set(datas)
        transaction = {}
        if results:
            for doc in results:
                transaction.update(doc.to_dict())
        return Response({"message":"transaction saved successfull"},data=transaction)
    except:
        return Response({"message":"transaction saved fails"})

@api_view(['GET'])
def getTransactions(request):
    results = Transaction.get()
    transactions = {}
    if results:
        for doc in results:
            transactions.update(doc.to_dict())
    return Response({"message":"Transactions saved successfull"},data=transactions)
