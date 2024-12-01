# HelpMeNow 
## Problem Statement
In today's world, personal safety is a growing concern, especially for individuals who may be vulnerable to various types of threats such as harassment, assault, or emergencies. In such situations, quick action is crucial, but many people may not always be able to contact help immediately, either due to physical incapacity, fear, or lack of awareness about their surroundings. Additionally, language barriers and technological limitations often make it harder for some individuals to report incidents effectively. Existing safety solutions may not always offer real-time location tracking, distress sound detection, or multilingual support, limiting their accessibility and effectiveness in emergencies.

Our problem was to create an easy-to-use and comprehensive solution that empowers individuals to respond effectively during emergencies by quickly notifying their emergency contacts, detecting distress sounds, and providing real-time location tracking. This solution needed to be accessible, user-friendly, and inclusive for all individuals, regardless of their language or technological expertise.

Innovative Idea and Solution
To address this problem, we developed HelpMeNow, a gender-neutral website designed to ensure the safety of individuals by integrating a variety of innovative features that provide immediate assistance during emergencies.

## Our innovative approach includes:


Our website uses crowd-sensing technology to identify the safest routes for users to follow and send notifications if they deviate from the route, helping individuals avoid potential dangers during emergencies.
Through this combination of AI, real-time tracking, and multilingual support, HelpMeNow provides an innovative and comprehensive approach to ensuring personal safety. By integrating these features, we aim to empower individuals to take control of their safety in any situation and communicate with others effectively during emergencies.

## Features
### SOS Button:

The website features an SOS button that, when pressed, sends an SMS to predefined emergency contacts and shares the user’s real-time location.
### Send SMS to Emergency Contacts:

When the SOS button is clicked, an SMS is automatically sent to the user’s emergency contacts, notifying them of the user's distress and location.
### Real-Time Location Tracking:

Upon pressing the SOS button, the website tracks and shares the user’s real-time location with emergency contacts, using the Leaflet API.
### Distress Sound Detection:

The website uses a speech model and TensorFlow for scream recognition, automatically triggering the SOS function when distress sounds (e.g., screams) are detected.
### Chatbot Integration:

A chatbot on the website assists users by performing safety-related actions. It is powered by Google API and OpenAI API. While OpenAI API is not yet fully implemented, we aim to complete this feature in future updates.
### Safe Route Detection:

Using Leaflet API and Twilio, the website can identify the safest route to the user’s destination based on crowd-sensing data and will alert users if they deviate from the route.
### Multilingual Support:

The website currently supports English, Malayalam, and Hindi, with plans to extend language support to reach a larger audience.
### Audio/Video Evidence:

The website can record audio and video for evidence. These media files can be kept for reference in case of emergency.


### HomePage
![Screenshot 2024-12-01 185315](https://github.com/user-attachments/assets/8c083075-cfe1-4687-8351-e296c3186d58)
![Screenshot 2024-12-01 185330](https://github.com/user-attachments/assets/b7bc10be-552e-4402-a479-c5f2f174cd53)

###Sign Up
![image](https://github.com/user-attachments/assets/b58fa5ec-ca00-4355-ada3-52d511111a66)

###Login
![image](https://github.com/user-attachments/assets/4985ea2c-3c8e-4363-a8bf-e390512148b8)

###Logged in
![image](https://github.com/user-attachments/assets/26dcf64a-6ae7-4c0d-b782-09e767cb61a5)




![image](https://github.com/user-attachments/assets/6be0b883-7624-4eec-a5ed-0f56ec090f85)

###Location Tracker
![image](https://github.com/user-attachments/assets/742d6581-53b4-4325-b674-276eebbdd263)

###Audio And Video Recording
![image](https://github.com/user-attachments/assets/8e8ac7c8-166e-4ab4-9f15-0d761cb8aa56)






## Future Enhancements
### Real-Time Location Sharing to Emergency Contacts & Police:

Future updates will enable the website to send live location data not only to emergency contacts but also to the nearest police station for immediate assistance.
### Safe Route Identification:

The website plans to improve its safe route detection feature by integrating more advanced crowd-sensing data and offering enhanced notifications when users stray from their path.
### Audio Recognition for Chatbot:

The chatbot will soon include an advanced audio recognition feature to detect distress sounds more accurately.
### Full Implementation of OpenAI API:

We are working on fully implementing OpenAI’s API for the chatbot to enhance its functionality.
### Multi-Language Support:

We aim to expand the website’s language options to make it accessible to a broader, global audience.
### Cloud-Based Audio/Video Evidence:

The website currently records audio and video for evidence. In future versions, we plan to allow users to upload this evidence to a cloud platform for safekeeping.
## AI Features
### Scream Recognition:

Using a speech model and TensorFlow, the website can recognize distress sounds such as screams and automatically trigger the SOS function.
### Chatbot:

The chatbot is powered by Google API and OpenAI API. While OpenAI API integration is still a work in progress, we plan to complete this feature in the near future.
### Safe Route Detection:

The website uses Leaflet API and Twilio for safe route detection, helping users find the safest path to their destination and alerting them if they deviate from it.
### Real-Time Location Tracker:

The real-time location tracker utilizes the Leaflet API to accurately share the user's location with emergency contacts.
## Challenges
### Geofencing and Crime Data:

A challenge faced was the inability to obtain necessary APIs for crime data from the Indian government, which limits the ability to use geofencing to detect dangerous areas based on crime statistics.
### Translation for Non-English Speakers:

We attempted to implement a translation feature using the Azure AI Translator API to help users who do not speak English report incidents. This feature is still a work in progress and aims to translate native languages into English for incident reporting.
## Current Limitations
The website can currently record audio and video for evidence but cannot upload this content to cloud services or other platforms. This feature is planned for future updates.
