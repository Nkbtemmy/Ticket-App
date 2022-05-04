import json
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from APIs.Database.index import Events
from APIs.response import response
from APIs.serializers import EventSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from APIs.decorators import authenticated_user, unauthenticated_user,allowed_role

token_Auth = openapi.Parameter('Authorization',in_=openapi.IN_HEADER,description="Description",type=openapi.TYPE_STRING)

@api_view(['GET'])
def default(request):
    return Response({"message":"Welcome to my events homepage"})

@swagger_auto_schema(method='post',request_body=EventSerializer, manual_parameters=[token_Auth], responses=response)
@api_view(['POST'])
@authenticated_user
# @allowed_role(['Admin,customer'])
def createEvent(request):
    try:
        body = {
            'name':request.data['name'],
            'description':request.data['description'],
            'photo':request.data['photo'],
            'location':{
                'room':request.data['room'],
                'seats':{
                    'section':request.data['section'],
                    'row': request.data['row'],
                    'seat':request.data['seat']
                }
            },
            'sponsers':request.data['sponsers'],
            'orgnaniser_id': request.id # this will be received from token
        }
        Events.document().set(body)
        datas = {"message":"Event created successful","status":status.HTTP_201_CREATED}
        return Response(data=datas,status=status.HTTP_201_CREATED)
    except requests.HTTPError as e:
        error_json = e.args[1]
        error = json.loads(error_json)['error']['message']
        return Response(data={"message":"event creation fails","error":error},status=status.HTTP_403_FORBIDDEN)
    
@swagger_auto_schema(method='get', manual_parameters=[token_Auth], responses=response)
@api_view(['GET'])
@authenticated_user
def viewEvents(request):
    try:
        results=Events.where("orgnaniser_id","==",f"{request.id}").stream() 
        datas = {"message":"Event retreived successful"}
        data =[]
        if results:
            for doc in results:
                new_doc = doc.to_dict()
                new_doc.update({"id":doc.id})
                data.append(new_doc)
            datas.update({"data":data})
        return Response(data=datas,status=status.HTTP_201_CREATED)
    except Exception as e:
        # error_json = e.args[1]
        # error = json.loads(error_json)['error']['message']
        # print(e)
        return Response(data={'message':"event failed to be retreived","status":status.HTTP_404_NOT_FOUND},status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def viewEvent(request,id):
    try:
        results=Events.where('id','==',id).get()
        datas = {"message":"Event retreived successful","status":status.HTTP_200_OK}
        if results:
            datas = results.to_dict()
            return Response(data=datas,status=status.HTTP_200_OK)
        return Response(data={"message":"there is no this user"},status=status.HTTP_404_NOT_FOUND)
    except requests.HTTPError as e:
        error_json = e.args[1]
        error = json.loads(error_json)['error']['message']
        return Response(data={"message":"Server Error","error":error,"status":status.HTTP_500_INTERNAL_SERVER_ERROR},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    