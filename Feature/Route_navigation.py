from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import os

app = Flask(_name_)

# Twilio credentials (use environment variables for security)
account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'your_account_sid')
auth_token = os.getenv('TWILIO_AUTH_TOKEN', 'your_auth_token')
twilio_number = os.getenv('TWILIO_PHONE_NUMBER', '+17754179181')  # Replace with your Twilio phone number

client = Client(account_sid, auth_token)


@app.route('/sendSOS', methods=['POST'])
def send_sos():
    try:
        # Parse incoming JSON request
        data = request.json
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        contacts = data.get('contacts')

        # Validate inputs
        if not latitude or not longitude or not contacts:
            return jsonify({"message": "Missing required data: latitude, longitude, or contacts"}), 400

        if not isinstance(contacts, list) or not all(isinstance(contact, str) for contact in contacts):
            return jsonify({"message": "Contacts should be a list of strings"}), 400

        # Send the SMS alert to each contact
        for contact in contacts:
            try:
                message = client.messages.create(
                    body=f"SOS Alert! Emergency at Location: Lat: {latitude}, Long: {longitude}",
                    from_=twilio_number,
                    to=contact
                )
                print(f"Message sent to {contact}. SID: {message.sid}")
            except TwilioRestException as e:
                print(f"Failed to send message to {contact}: {str(e)}")

        return jsonify({"message": "SOS alert sent to emergency contacts!"}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"message": "Internal server error"}), 500


if _name_ == "_main_":
    # Run Flask app
    app.run(debug=True)
