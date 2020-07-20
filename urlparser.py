import requests
import pprint
from bs4 import BeautifulSoup
import sendtext as st

starting_url = 'https://seths.blog/2020/07/commercial-vulnerability/'
url = 'https://seths.blog/2020/07/commercial-vulnerability/'
page = requests.get(url)
pp = pprint.PrettyPrinter(indent=4)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div', class_='has-content-area')
paragraphs = results.find_all('p')


for paragraph in paragraphs:
    st.telegram_bot_sendtext("te kutya")
