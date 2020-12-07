# Alexa-Skills
Making Raspberry pi the local automation hub for older devices. 

This repo contains a basic flask server, utilizing the Flask-Ask package to interface with Alexa. 
To further make this happen I utilize "ngrok" (on the pi its the Linux ARM) download to open up a tunnel.
I then create an Alexa skill (in the Amazon developer console) that points to the ngrok endpoint. 
This skill should be fully defined in the included JSON file incase something happens to the console
