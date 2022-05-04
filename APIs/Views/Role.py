from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from APIs.Database.index import Role

@api_view(['GET'])
def default(request):
    return Response({"message":"Welcome to Role Page"})

@api_view(['POST'])
def saveRoles(request):
    data = request.data
    results = Role.document().set(data)
    Roles = {}
    if results:
        for doc in results:
            Roles.update(doc.to_dict())

    return Response({"message":"Roles saved successfull"},data=Roles)


@api_view(['GET'])
def getRoles(request):
    results = Role.get()
    events = {"message":"Roles retreived successfully"}
    if results:
        for doc in results:
            events.update(doc.to_dict())
    return Response(data=events)
