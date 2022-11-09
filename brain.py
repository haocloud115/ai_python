# KNOW + SPEAK + LISTEN (BE LEARNT BY DUNG LAI LAP TRINH--)

# Import lib
import speech_recognition
import pyttsx3
from datetime import date, datetime

while True:
    
    # var
    robot_ear = speech_recognition.Recognizer()
    robot_mouth = pyttsx3.init()
    robot_brain = ""

    # listen
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    
    try:  
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    # know
    if "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %y")
    elif you == "":
        robot_brain = "I can't here what you say"
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hour %M minutes %S seconds")
    elif "name" in you:
        robot_brain = "My name is Tanaki and Your name is Tanaka"
    elif "bye" in you:
        robot_brain = "Bye my friend"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "end" in you:
        robot_brain = "Bye my friend"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    elif "developer staff" in you:
        robot_brain = "My owner is Tanaka Rin"
    elif "language" in you:
        robot_brain = "I'm written by Python"
    else:
        robot_brain = "Hello, I'm Tanaki"
        
    # speak
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()