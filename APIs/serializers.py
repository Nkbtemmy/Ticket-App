from rest_framework import serializers
from .models import Payment,Organiser,Event, Ticket

class OrganiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organiser 
        fields = [ "name","address","description","role","email","password"]
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organiser 
        fields = [ "email","password"]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name','description','photo','room','section','row','seat','sponsers','starting_date_time','ending_date_time']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields =  ['name','description','price','quantity','sales_start_date_time','sales_end_date_time','qr_code','ticket_type','checkout']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'