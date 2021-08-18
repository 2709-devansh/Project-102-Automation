import pyttsx3
import os

file = input("Enter File Path: ")
with open(file, 'r') as f:
    data = f.readlines()
    print(data)

engine = pyttsx3.init()
engine.say(data) 
engine.runAndWait()

