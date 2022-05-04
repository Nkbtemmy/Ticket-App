from email.policy import default
from django.db import models
import uuid
import datetime

# Create your models here.
class Organiser(models.Model):
    roles = [
        ('admin','admin'),
        ('organiser','organiser'),
        ('customer','customer'),
        ('agent','agent'),
    ]
    Organiser_id = models.UUIDField(auto_created=True,default=uuid.uuid4, editable=False, primary_key=True,unique=True, serialize=False, verbose_name='organiserId')
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    description=models.TextField(max_length=2000)
    password = models.TextField(max_length=500)
    role = models.CharField(max_length=100,choices=roles)
    deleted = models.BooleanField(default=False)
    email=models.EmailField(unique=True)
    createAt=models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    eventId = models.UUIDField(auto_created=True,default=uuid.uuid4, editable=False, primary_key=True, unique=True, serialize=False, verbose_name='eventId')
    orgnaniser_id = models.ForeignKey(Organiser,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    photo= models.TextField()
    room = models.TextField(name='room')
    section = models.TextField(name='section')
    row = models.TextField(name='row')
    seat = models.TextField(name='seat')
    sponsers = models.JSONField(default=[])
    starting_date_time = models.DateTimeField(auto_now_add=True)
    ending_date_time = models.DateTimeField(auto_now_add=True)
    createAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)
    open = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Ticket(models.Model):
    ticketId = models.UUIDField(auto_created=True,default=uuid.uuid4, editable=False, primary_key=True, unique=True, serialize=False, verbose_name='eventId')
    organiser_id = models.ForeignKey(Organiser,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.FloatField(null=False, default=0)
    quantity = models.FloatField(null=False,default=1)
    sales_start_date_time = models.DateTimeField(default=datetime.datetime.now())
    sales_end_date_time = models.DateTimeField(default=datetime.datetime.now())
    qr_code = models.TextField()
    ticket_type = models.CharField(max_length=100)
    checkout = models.BooleanField(default=False)

class Payment(models.Model):
    types = [
        ('MTN','MTN'),
        ('Card','Card'),
        ('Airtel','Airtel'),
        ('Spens','Spenn'),
    ]
    transactionId: models.UUIDField(auto_created=True,default=uuid.uuid4, editable=False, primary_key=True, unique=True, serialize=False, verbose_name='eventId')
    transaction_Date_time = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    payment_type = models.CharField(null=False, choices=types,max_length=100)