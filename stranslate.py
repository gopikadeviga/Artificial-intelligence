import pandas as p
from googletrans import Translator #import translator class from googletrans module for translation
import time #adding dely in the script as it arised error while execting it continuously

#creating an object for the translator class
t = Translator()

# read the summary.csv file that contains the scrapped data
#this dataframe contains data to be translated
df = p.read_csv('summary.csv')

# translate page name and summary to hindi tamil and malayalam
languages = ['hi', 'ta', 'ml']

#this is the functin for translation 
# takes the text as an argument and the language to which that text should be transkated as another agument
def translatet(text, lang):
    try:
        translation = t.translate(text, dest=lang)
        return translation.text
    except Exception as e:
        print(f"Error translating: {e}")
        return ''

#looping the language in the list
#translate pagename and summary
for lang in languages:
    #f -creating formatted string in python
    #apply method applies the teanslatet function for each pagename 
    #creates new column in the translated csv file which contains languages translated to
    df[f'Translated Page Name ({lang})'] = df['Page Name'].apply(translatet, args=(lang,))
    #this creates for summary
    df[f'Translated Summary ({lang})'] = df['Summary'].apply(translatet, args=(lang,))
    
    # dely for 2 sec
    time.sleep(2)

# saving the translated data to a new csv file without the index
df.to_csv('translated.csv', index=False)
print('Data translated and saved successfully.')
