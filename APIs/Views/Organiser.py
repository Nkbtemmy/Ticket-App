import json
from grpc import StatusCode
import requests
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from APIs.serializers import OrganiserSerializer, LoginSerializer
from APIs.Database.main import auth
from APIs.Database.index import Organiser, database, Events
from APIs.decorators import authenticated_user, unauthenticated_user,allowed_role
from APIs.response import response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class Controllers:
    serializer_class = OrganiserSerializer
    token_Auth = openapi.Parameter('Authorization',in_=openapi.IN_HEADER,description="Description",type=openapi.TYPE_STRING)
    test_param = openapi.Parameter('id', openapi.IN_QUERY, description="id manual param", type=openapi.TYPE_BOOLEAN)

    
    @api_view(['GET'])
    def default(request):
        return Response({"message":"Welcome to organiser homepage"})

    @swagger_auto_schema(method='post',request_body=serializer_class, manual_parameters=[], responses=response)
    @api_view(['POST'])
    @unauthenticated_user
    def signup(request):
        try:
            email = request.data['email']
            password = request.data['password']
            role = 'customer'
            if request.data.get('role'):
                role = request.data['role'] 
            user = auth.create_user_with_email_and_password(email,password)
            Organiser.document(user['localId']).set({
                "email":email,
                "name": request.data['name'],
                "address":request.data['address'],
                "description":request.data['description'],
                "role":role

            })
            result = {
                "access_token":user["idToken"],
                "refreshToken":user["refreshToken"],
                "expiresIn":user["expiresIn"],
            }
            return Response(data=result,status=status.HTTP_201_CREATED)
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            return Response(data={'message':"signup fails","error":error},status=status.HTTP_306_RESERVED)

    @swagger_auto_schema(method='post',request_body=LoginSerializer, manual_parameters=[], responses=response)
    @api_view(['POST'])
    @unauthenticated_user
    def login(request):
        try:
            email = request.data['email']
            password = request.data['password']
            user = auth.sign_in_with_email_and_password(email,password)
            # customerToken = authe.create_custom_token(uid=user['localId'],developer_claims={'role':'admin'})
            datas={
                'id_token':user['idToken'],
                'refresh_token':user['refreshToken'],
                'expires_in':user['expiresIn'],
                "status":status.HTTP_200_OK
            }
            return Response(data= datas)
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            return Response(data={'message':'Username/Password is incorrect',"status":status.HTTP_401_UNAUTHORIZED,"error":error},status=status.HTTP_306_RESERVED)
    
    @swagger_auto_schema(method='delete', manual_parameters=[token_Auth,], responses=response)
    @api_view(['DELETE'])
    @authenticated_user
    @allowed_role(['admin'])
    def delete(request,pk):
        try:
            # user_id = request.id
            Organiser.document(pk).update({"deleted":True})
            data = Organiser.document(pk).get()
            print(data)
            return Response(data= {"message":"organiser deleted successfull",},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(data= {'message':'Login fails'},status=status.HTTP_401_UNAUTHORIZED)
    

    @api_view(["GET"])
    def getAllOrganiser(request):
        try:
            all_oragnisers = Organiser.stream()
            datas = {"status":status.HTTP_200_OK,"message":"Organiser retreived successful"}
            data =[]
            if all_oragnisers:
                for doc in all_oragnisers:
                    new_doc = doc.to_dict()
                    new_doc.update({"id":doc.id})
                    data.append(new_doc)
                datas.update({"data":data})
            return Response(data=datas,status=status.HTTP_200_OK)
        except:
            return Response(data={"message":"failed to retreive Organisers","status":status.HTTP_400_BAD_REQUEST})
    
    @api_view(['GET'])
    def getOneOrganiser(request,id):
        try:
            organiser = Organiser.document(id).get()
            datas = {"message":"Organiser retreived successful"}
            if organiser:
                datas = organiser.to_dict()
                return Response(data=datas,status=status.HTTP_200_OK)
            return Response(data={"message":"there is no this user"},status=status.HTTP_404_NOT_FOUND)
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            return Response(data={"message":"Server Error","error":error,"status":status.HTTP_500_INTERNAL_SERVER_ERROR},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @swagger_auto_schema(method='get', manual_parameters=[token_Auth,], responses=response)
    @api_view(['GET'])
    @authenticated_user
    def organiserProfile(request):
        try:
            organiser = Organiser.document(request.id).get()
            print(organiser.to_dict())
            datas = {"message":"Organiser retreived successful","status":status.HTTP_200_OK}
            if organiser:
                datas = organiser.to_dict()
                return Response(data=datas,status=status.HTTP_200_OK)
            return Response(data={"message":"there is no this user"},status=status.HTTP_404_NOT_FOUND)
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            return Response(data={"message":"Server Error","error":error,"status":status.HTTP_500_INTERNAL_SERVER_ERROR},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

     