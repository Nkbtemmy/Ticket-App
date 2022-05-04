import pyrebase
project_id= "hexakomb-abb9d"
client_id= "116560888800993642732",
client_email = "firebase-adminsdk-i6g14@hexakomb-abb9d.iam.gserviceaccount.com",
firebaseConfig = {
  "apiKey": "AIzaSyCWChI7GpcEqkj1Ux99vs47N7UAw9XyEa8",
  "authDomain": "hexakomb-abb9d.firebaseapp.com",
  "projectId": "hexakomb-abb9d",
  "databaseURL":"https://hexakomb-abb9d-default-rtdb.firebaseio.com",
  "storageBucket": "hexakomb-abb9d.appspot.com",
  "messagingSenderId": "662750758945",
  "appId": "1:662750758945:web:3f6e57a458b1e2fb6fbb60",
  "measurementId": "G-PB119EKC41",
  'serviceAccountId': '116560888800993642732@hexakomb-abb9d.iam.gserviceaccount.com',
#   "service_account_email":client_email
#   'my-client-id@my-project-id.iam.gserviceaccount.com',
}

firebase = pyrebase.initialize_app(firebaseConfig)

# db = firebase.database();
auth = firebase.auth();
# storage = firebase.storage();


# # import firebase_admin
# # from firebase_admin import credentials
# # from firebase_admin import firestore

# # # Use the application default credentials
# # cred = credentials.ApplicationDefault()
# # firebase_admin.initialize_app(cred, firebaseConfig )

# # db = firestore.client()