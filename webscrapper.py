import requests # make http req
from bs4 import BeautifulSoup as bs #used for webscrapping
import pandas as p #tabular format

# URL to scrape
url = "https://www.nueverainfotech.com/contact"

# get the information in the url using get() function and store the response
response = requests.get(url)

# status code 200 means the request was succesfull
if response.status_code == 200:
    # as it is successfull create an object for bs to parse htmlcontent of web page (html.parser)
    soup = bs(response.text, 'html.parser')

    # extraction the title of the page as the Pagename to be stored in csv
    #.text is to retrive the text content of the tag
    #strip() remove whitespces (leading/trialing)
    page_name = soup.title.text.strip()

    # the summary was written inside the mata tag with name="description" 
    # so use soup.find() to find that in the html page and store it in a variable
    meta_tag = soup.find('meta', attrs={'name': 'description'})

    # if mata tag with the specified name exist then extract the content specified in it and store that in the summary variable
    # if not summary should be set to empty string
    summary = meta_tag.get('content') if meta_tag else ""

    # Creating datafarme of the csv file using pandas with three fields
    # each one will be a list containing sinle value
    data = p.DataFrame({'Page Name': [page_name], 'URL': [url], 'Summary': [summary]})

    # Save the data to a CSV file
    #index is set to false because it should not be included in the csv file
    data.to_csv('summary.csv', index=False)

    print("Data scraped successfully and saved to 'summary.csv'.")
else:
    print("Failed to retrieve data from the URL.")
