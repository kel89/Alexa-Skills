# Alexa-Skills
Making Raspberry pi the local automation hub for older devices. 

This repo contains a basic flask server, utilizing the Flask-Ask package to interface with Alexa. 
To further make this happen I utilize "ngrok" (on the pi its the Linux ARM) download to open up a tunnel.
I then create an Alexa skill (in the Amazon developer console) that points to the ngrok endpoint. 
This skill should be fully defined in the included JSON file incase something happens to the console

Note: I was following [this site](https://www.hackster.io/nishit-patel/controlling-raspberry-pi-using-alexa-33715b#:~:text=Head%20over%20to%20'test'%20section,you%20skill%20on%20your%20device.) and the corresponding [repo](https://github.com/nishitpatel28/Controlling-Raspberry-Pi-using-Alexa)

Also note: [this thread](https://github.com/bwssytems/ha-bridge/issues/619) has some hot tips for Denon commands (all in URL).
