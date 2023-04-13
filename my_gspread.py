import requests
from bs4 import BeautifulSoup
import gspread
import re
import os
from oauth2client.service_account import ServiceAccountCredentials

# Set a path of API key json faile as a system environment 
api_key = os.environ.get('API_KEY')
print(api_key)
# authenticate with Google Sheets API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(api_key, scope)
client = gspread.authorize(creds)

# open the Google Sheets document
sheet = client.open('gspread').sheet1

# specify the URL of the website to scrape
url = 'https://www.leiloesbr.com.br/busca.asp?pesquisa=diamondg&gbl=0&op='

# send a GET request to the website and parse the HTML
response = requests.get(url)
# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

# # find all the relevant items on the page
items = soup.find_all('div', class_=re.compile('item'))

print(items[0])

# iterate over the items and extract the relevant information
for item in items:
    title = item.find('a', class_='item-title')#.text
    # description = item.find('div', class_='description')#.text
    price = item.find('div', class_='item-price')#.text

    # add the information to the Google Sheets document
    # row = [title, description, price]
    row = [title, price]
    # row = ["test", "test2"]
    print(row)
    # sheet.append_row(row)
    sheet.append_row(row)
