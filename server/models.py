#!/usr/bin/env python3
from app import db

class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email
        }
