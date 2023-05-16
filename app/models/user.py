from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.BigInteger,primary_key=True, autoincrement=True)
    name = db.Column(db.String(40),nullable = False)
    email = db.Column(db.String(40),index=True,unique=True,nullable=False)
    password = db.Column(db.String(10),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow)