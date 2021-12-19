import pyttsx3
robot_brain = "I can't hear you, please speak again!"

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()