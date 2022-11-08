import pyttsx3

robot_brain = "Hello Tanaka Rin"

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
