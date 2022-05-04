# from django.http import Response
import json
import requests
from rest_framework.response import Response
from rest_framework import status
from APIs.Database.main import auth
from APIs.Database.index import Organiser

def unauthenticated_user(view_func):
    def wrapper_fun(request, *args, **kwargs):
        if request.headers.get('Authorization'):
            return Response(data={"message":"you are already loged in"})
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_fun

def authenticated_user(view_func):
    def wrapper_fun(request, *args, **kwargs):
        headers = request.headers
        if 'Authorization' in headers:
            try:
                token = request.headers.get('Authorization')
                decoded_token = auth.get_account_info(token)
                request.id = decoded_token['users'][0]['localId']
                return view_func(request, *args, **kwargs)

            except requests.HTTPError as e:
                error_json = e.args[1]
                error = json.loads(error_json)['error']['message']
                return Response(data={'message':"token is expired or incorrect","error":error},status=status.HTTP_306_RESERVED)
        else:
            return Response(data={
                "message":"you need to login first",
                "status":status.HTTP_401_UNAUTHORIZED
            })    
    return wrapper_fun

def allowed_role(allowed_roles = []):
    def decorater(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            doc_ref = Organiser.document(request.id)
            doc = doc_ref.get()
            if doc.exists:
                data =doc.to_dict()
                # print(f'Document data: {doc.to_dict()}')
                group = data['role']
            else:
                print(u'No such document!')
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return Response(data={"message":'you are not authorized to view this page'},status=status.HTTP_401_UNAUTHORIZED)
        return wrapper_func
    return decorater