import speech_recognition
import arrow
import pyttsx3
from datetime import datetime
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
while True:
	with speech_recognition.Microphone() as mic:
		print("De Tu cua Binh: I'm listening")
		audio = robot_ear.listen(mic)
	print("De Tu cua Binh:...")	
	try:	
		you = robot_ear.recognize_google(audio)
	except: 
		you = ""
	print("You: "+ you)

	if you == "":
		robot_brain = "I can't hear you, please say again!"
	elif "how old are you" in you:
		robot_brain = "18"
	elif "your name" in you:
		robot_brain = "De tu cua Binh" 		
	elif "hello" in you:
		robot_brain = "hello there"
	elif "how are you" in you:
		robot_brain = "I'm fine thank you and you!"	
	elif "today" in you:
		robot_brain =arrow.now().format('DD-MM-YYYY')
	elif "time" in you :
		now = datetime.now()
		robot_brain = current_time = now.strftime("%H:%M:%S")
	elif "tired" in you :
		robot_brain = "You should to go to bed"
	elif "bye" in you:
		robot_brain = "Good Bye"
		print("De Tu cua Binh: "+robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait()
		break	
	else:
		robot_brain = "I don't know sorry!"

	print("De Tu cua Binh:"+robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait()

