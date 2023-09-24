#!/usr/bin/env python3
from app import db
from models import Newsletter

def seed_data():
    with db.app.app_context():
        db.create_all()

        email1 = Newsletter(email='example1@example.com')
        email2 = Newsletter(email='example2@example.com')

        db.session.add(email1)
        db.session.add(email2)
        db.session.commit()

if __name__ == '__main__':
    seed_data()
