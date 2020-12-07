
import logging
import os
import requests

from flask import Flask
from flask_ask import Ask, request, session, question, statement

# setup the app
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

# Denon Controls
denon_ip = "192.168.0.29"
denon_url = "http://" + denon_ip + "/MainZone/index.put.asp"

def denon_volume_up():
	url = denon_url + "?cmd0=PutMasterVolumeBtn/>"
	print(url)
	requests.get(url)

def denon_volume_down():
	url = denon_url + "?cmd0=PutMasterVolumeBtn/<"
	requests.get(url)
	
def denon_mute():
	url = denon_url + "?cmd0=PutVolumeMute/on"
	requests.get(url)
	
def denon_unmute():
	url = denon_url + "?cmd0=PutVolumeMute/off"
	requests.get(url)

def denon_set_volumne(vol):
	level = vol - 80
	url = denon_url + "?cmd0=PutMasterVolumeSet/" + str(level)
	requests.get(url)
	
def denon_on():
	url = denon_url + "?cmd0=PutZone_OnOff/ON"
	requests.get(url)

def denon_off():
	url = denon_url + "?cmd0=PutZone_OnOff/OFF"
	print(url)
	requests.get(url)

def denon_firetv_input():
	url = denon_url + "?cmd0=PutZone_InputFunction/BD"
	requests.get(url)

# Intents----------------
@ask.launch
def launch():
	say = 'Welcome to the Pi'
	return question(say).reprompt(say).simple_card(say)
	
@ask.intent('AMAZON.HelpIntent')
def help():
	say = 'You can ask me to control the receiver'
	return question(say).reprompt(say).simple_card(say)


@ask.session_ended
def session_ended():
	return "{}", 200
	
	
@ask.intent('WhatsGoodIntent')
def whats_good():
	return statement("Whats good my man")
	
@ask.intent('HelloWorldIntent')
def hello_world():
	return statement("Hello world test passed").simple_card("Hello world")


@ask.intent("VolumeUp")
def vol_up():
	print("Turning volume up")
	denon_volume_up()
	return statement("Volume turned up a notch").simple_card("Volume up a notch")
	
@ask.intent("VolumeDown")
def vol_down():
	denon_volumne_down()
	return statement("Its louder")

@ask.intent("SetVolume", convert={'level':int})
def set_vol(level):
	denon_set_volumne(level)
	return statement("Volume set to " + str(level)) #\
		#.simple_card("Volumne set to " + str(level))
		
@ask.intent("ReceiverOff")
def turn_denon_off():
	denon_off()
	text = "Receiver off"
	return statement(text).simple_card(text)
	
@ask.intent("ReceiverOn")
def turn_denon_on():
	denon_on()
	text = "Receiver on"
	return statement(text).simple_card(text)
	
@ask.intent("Mute")
def mute():
	denon_mute()
	text = "Muted"
	return statement(text).simple_card(text)
	
@ask.intent("Unmute")
def unmute():
	denon_unmute()
	text = "Unmuted"
	return statement(text).simple_card(text)
	
@ask.intent("InputFireTV")
def change_input():
	denon_firetv_input()
	text = "Input changed to Fire TV"
	return statement(text).simple_card(text)


# Test Web Routes--------------
@app.route('/')
def web_test():
	return "Web test good"
	
@app.route("/on")
def on():
	denon_on()
	return "should be on"
	
@app.route("/off")
def off():
	denon_off()
	return "should be off"

if __name__ == "__main__":
	if 'ASK_VERIFY_REQUESTS' in os.environ:
		verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
		if (verify == 'false'):
			app.config['ASK_VERIFY_REQUESTS'] = False
	
	app.run(debug=True)
