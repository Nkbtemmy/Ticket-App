import json
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from APIs.Database.index import Ticket
from APIs.decorators import authenticated_user, unauthenticated_user,allowed_role
from APIs.response import response
from APIs.serializers import TicketSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


token_Auth = openapi.Parameter('Authorization',in_=openapi.IN_HEADER,description="Description",type=openapi.TYPE_STRING)


@api_view(['GET'])
def default(request):
    return Response({"message":"Welcome to Ticket page"})

@swagger_auto_schema(method='post',request_body=TicketSerializer, manual_parameters=[token_Auth], responses=response)
@api_view(['POST'])
@authenticated_user
# @allowed_role(['Admin,customer'])
def saveTicket(request):
    try:
        data = {
            "name":request.data['name'],
            "description":request.data['description'],
            "price":request.data['price'],
            "quantity":request.data['quantity'],
            "sales_start_date_time":request.data['sales_start_date_time'],
            "sales_end_date_time": request.data['sales_end_date_time'],
            "qr_code":request.data['qr_code'],
            "ticket_type":request.data['ticket_type'],
            "checkout":request.data['checkout'],
            "organiser_id":request.id
        }
        Ticket.document().set(data)
        return Response(data={"message":"Tickets saved successfull","status":status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)

    except requests.HTTPError as e:
        error_json = e.args[1]
        error = json.loads(error_json)['error']['message']
        return Response(data={"message":"Tickets failed to be created","error":error,"status":status.HTTP_403_FORBIDDEN},status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def getTickets(request):
    try:
        all_tickets = Ticket.stream()
        datas = {"status":status.HTTP_200_OK,"message":"Tickets retreived successful"}
        data =[]
        if all_tickets:
            for doc in all_tickets:
                new_doc = doc.to_dict()
                new_doc.update({"id":doc.id})
                data.append(new_doc)
            datas.update({"data":data})
        return Response(data=datas,status=status.HTTP_200_OK)
    except requests.HTTPError as e:
        error_json = e.args[1]
        error = json.loads(error_json)['error']['message']
        return Response(data={"message":"failed to retreive Tickets","error":error,"status":status.HTTP_500_INTERNAL_SERVER_ERROR},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    