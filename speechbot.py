#  Implementation of speech recognition feature in the chatbot
# Using speech_recognition library
import speech_recognition as sr

# Initializing the recognizer
recognizer = sr.Recognizer()

# Capture the audio through microphone
# Microphone is the subclass of audio source
with sr.Microphone() as m:
    print("Say something:")
    audio = recognizer.listen(m)

try:
    # Recognize speech using Google speech recognition api - recognize_google
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, could not understand audio")
