import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

class FirebaseService:
    def __init__(self, credentials_path, database_url):
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred, {'databaseURL': database_url})

    def upload_to_firebase(self, data):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
        ref = db.reference(f'/sensor/{timestamp}')
        ref.set(data)