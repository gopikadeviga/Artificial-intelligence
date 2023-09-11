#using flask 
#Flask - core component, request - for http request, render_template- rendering html template 
from flask import Flask, request, render_template
import pandas as p
from gtts import gTTS #google text to speech
import os 
import webbrowser

#naming the flask application
#__name__ - rurrent module name and allows to determine the root path itself
tab = Flask(__name__)

# reading csv file
df = p.read_csv('translated.csv')

languages = ['hi', 'ta', 'ml']

# route decorator for the root URL ('/')
@tab.route('/')
#index() will be executed when accessing the root url
def index():
    #rendring the template and return the response
    #index.html will be the template with the html form to be submitted
    return render_template('index.html')

#/info url to accept post request
@tab.route('/info', methods=['POST'])
#getting the information provided in the form
def info():
    pagename = request.form['pagename']
    selected_language = request.form['language']

    #searching for the provided pagename match
    row = df[df['Page Name'] == pagename]

    if not row.empty:
        # creating a diationary to store the translated datas
        translations = {
            selected_language: {
                #key-value creation row.iloc[0] means indexing the df 0 mens first row
                'Translated Page Name': row.iloc[0][f'Translated Page Name ({selected_language})'],
                'Translated Summary': row.iloc[0][f'Translated Summary ({selected_language})']
            }
        }

        #generate text to speech and save it
        tts_text = f"Translated Page Name: {translations[selected_language]['Translated Page Name']}. Translated Summary: {translations[selected_language]['Translated Summary']}"
        tts = gTTS(tts_text, lang=selected_language)
        tts.save('output.mp3')

        # Play the TTS audio
        os.system('start output.mp3')

        # Open the URL in a web browser
        url = row.iloc[0]['URL']
        webbrowser.open(url)

        return render_template('output.html', translations=translations)
    else:
        return "Page not found."

# run as main program in debug mode
if __name__ == '__main__':
    tab.run(debug=True)
