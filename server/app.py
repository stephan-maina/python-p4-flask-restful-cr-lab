#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Newsletter  # Import the Newsletter model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newsletter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/api/newsletters', methods=['POST'])
def create_newsletter():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({'message': 'Email is required'}), 400

    # Create a new newsletter entry
    new_email = Newsletter(email=email)
    db.session.add(new_email)
    db.session.commit()

    return jsonify({'message': 'Newsletter subscription created successfully'}), 201

@app.route('/api/newsletters', methods=['GET'])
def get_newsletters():
    newsletters = Newsletter.query.all()
    newsletter_list = [email.to_dict() for email in newsletters]

    return jsonify(newsletter_list)

if __name__ == '__main__':
    app.run(debug=True)
