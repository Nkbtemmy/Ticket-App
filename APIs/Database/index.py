import firebase_admin
from firebase_admin import credentials,firestore,auth


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
database= firestore.client()
Events = database.collection("Events")
Organiser = database.collection("Organisers")
Ticket = database.collection("Tickets")
Transaction = database.collection("Transactions")
Role = database.collection("Roles")
