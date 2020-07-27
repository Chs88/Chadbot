# Chadbot
Python Telegram bot that sends you a random blog post from Seth Godin's blog. 


Prerequisites: 
- A bot previously created in Telegram app
- Registration to the openweathermap API (https://openweathermap.org/api)
- pip install beautifulsoup4
- pip install python-decouple
- A .env file with the following variables:
CHAT_ID=[Chat ID you received when registered for Telegram]
BOT_TOKEN=[API token for the Telegram bot]
WEATHER_API=[Openweathermap API token]
CITY=[The city you want the weather report for]
NAME=[Your name]
STARTING_PAGE="https://seths.blog/2020/07/fake-deadlines/" [could be any post]
