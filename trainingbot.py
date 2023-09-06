import pandas as p
import speech_recognition as sr
import webbrowser
# library for converting text to speech
import pyttsx3  
import re 

data = p.read_csv('website_summary.csv')
recognizer = sr.Recognizer()


speech = pyttsx3.init()

# Function to speak the text
def speak(text):
    speech.say(text)
    speech.runAndWait() # wait till user speaks

def recognize():
    with sr.Microphone() as mic:
        print("Listening for a page name...")
        user_speech = recognizer.listen(mic)
    try:
        input = recognizer.recognize_google(user_speech)
        return input
    except sr.UnknownValueError:
        return "Try again"

# find a pageurl and summary based on the input
def page_info(input, data):
    # removing spaces and characters from input using regular expr
    removed = re.sub(r'[^A-Za-z0-9]+', '', input)
    #ignring the index using _
    for _, row in data.iterrows():
        pnremoved = re.sub(r'[^A-Za-z0-9]+', '', str(row['Page Name']))
        if removed.lower() == pnremoved.lower():
            return row['URL'], row['Summary']
    # for both url and summary (cannot unpack non-iterable NoneType object) encountered this error while using only one None
    return None,None  

pdf_link = "https://www.nueverainfotech.com/_files/ugd/f36f8e_6eda1dbf2f304ac88351bada06425ca5.pdf"

# use while True: if need to loop throug it
input = recognize()

if "exit" not in input.lower():
      url, summary = page_info(input, data)
      if url:
          speak("Opening the website.")
          webbrowser.open(url)
          if summary:
              speak("Here is the summary.")
              speak(summary)
      else:
           webbrowser.open_new(pdf_link)
           error_message = "Sorry, I didn't catch that. Refer to this PDF for your queries"
           speak(error_message)
