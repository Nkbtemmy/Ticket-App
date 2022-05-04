import firebase_admin
from firebase_admin import credentials,firestore,auth

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "hexakomb-abb9d",
  "private_key_id": "13da37ca906e973cbcfa6553937d9234c9233749",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC3VSHgOhyvPFwI\nWEzN9bCVSlrch6uAMwO6BuYoHcRBiWyFMhq1RRU+7GPhaLzLViWyDZ4eGDHROUi/\nuzpM6fdI4e0PhbMdJ0iF/3YPLHMoljEkdew2k++uksagzT6tsZwQ1vnzg9E+cKRi\nXQ2MyBcfZrXoBUJKNv/ufGvqq+h5waQ+0Ub18S+XftoYmyiLpWdKZ/SiS32GOkSg\ng38YyNL1FA1PakMyBPY/IFF+lrPxMkMN2WDuasti9KL66fpeHpqYYHsePuf0YNEa\nogVkkUDL85G1Eclw9JS97Pmfg5E5Pz91uLWfGTnqky0ULxeXMKpjHPjuYPiuOZwA\nT0heg4/xAgMBAAECggEAA8i/UgJJEMnpaWevMCoj2rUF8prfTJ5g85BMZGQW5rZo\nNcieugKiyWF2P1Ma4ISW8xmqW5sqvhOVX5XFAozqxIebTdB37cBflBp9jJshhmMx\nQPwpI8hCcINJk8ygwFOT8doKHz9njIclMX2Tt8XyijyjwRYItAD2H+1UCexB+G9g\nl4CMJD2AK557V6KToxi92lPOzLuXr4bBJ2A3GdE/9Q8PWoFCDfSNTRQi6l7rx1gj\nFAU5glg8C68gbhPGholHil0amYtsgZyQo28KsrNODr/16aTwb7ojlSGZeBZA56Vj\nwjkgTwxsaEwOAzjKHHqQGHhqkOFQdFd4CjgvCW589QKBgQDmOl7Y4CYZoy0mhxJs\nkI0Bs8mt3MYhu6pUdz4JsFMDvrIrpFMcz2sgWc5psO6jyEZuMlEmVakZG52vze9K\nk++T+ewbQienWLJInm7MO8cXmK+/GPcgkQh2mXJrAQ9KxoWEDa/MSZIY0RarpWUV\nwlzlLz+ITuhe86ijUvd3n8GpPQKBgQDL2uGtqf3qK0QJLemTZwjjbDJ6VTmU66Tc\n4YZ36MvE1xg8HV9uEX1aY6b4yWHTRIT98OgfbVOHnpiMeN/joYh5+8WdSeUwCuWC\nMWogXq0oYrbmUZHqXncPGABhiygPBMQolDKiPWcPjYAK6eHuSdd+a0OT3GIQf0zR\nkAPiaurkxQKBgQC/p+XfSzHMc9+ZTCZVRDxuJ1oEJ161JEHWUPHPJP7mhjBSTlh2\nCmGWq8w+hfETXRzsjWyqqfK8GRY7DQdgISj3Gb2or3jNQfQgqet4j2bcyNm9Dq5j\naPkPqgvq8hXl3L+3P6GSQciiaiUiPOyaoZOtopiUA4RDzzkaxW2HIvIXzQKBgQCo\nkOXsZJTB/eTUclKiwKBo7h8PaUmkCvbYbuRyYt2cdwBjNSakLXIqPBzlvCBYQmB2\nW66VziE0E8Cw54K7B+eCdt6BoYkSoPAHKDVJbwBgVMBI00qFMnfg00f9YMRPJvHN\nXD5CSePeyHMIkz1vfT/kGW5X5fRxD9LFtwB/SUnSwQKBgQCgRctV1Vbu+UMRfDxS\nLVe6zK8wz4NZUlPfT2jnnIATtcjWmU2q2QMXaUV/8dvysnsU5dZnveJS7tHJkhhL\nqgmaw+hLCB9cHR2ECBWmOss4nruicnaVbIZzuyQR6IlzxcOCSwqoKTObCyqWVsiN\nIyaETsg4ykEuaYqcttGaqpTCBQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-i6g14@hexakomb-abb9d.iam.gserviceaccount.com",
  "client_id": "116560888800993642732",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-i6g14%40hexakomb-abb9d.iam.gserviceaccount.com"
}
  )
firebase_admin.initialize_app(cred)
database= firestore.client()
Events = database.collection("Events")
Organiser = database.collection("Organisers")
Ticket = database.collection("Tickets")
Transaction = database.collection("Transactions")
Role = database.collection("Roles")
