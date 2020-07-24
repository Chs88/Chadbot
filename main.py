# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import date
from decouple import config
import json


class Chadbot:
    def __init__(self):
        self.name = "Chadbot"
        self.url = self.get_random_url()
        self.today = date.today()
        self.DotW = self.day_of_the_week()  # Day of the week

    def sendtext(self, bot_message):
        bot_token = config('BOT_TOKEN')
        bot_chatID = config('CHAT_ID')
        send_text = 'https://api.telegram.org/bot' + bot_token + \
            '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)

    def send_blogpost(self, blog_post):
        for item in blog_post:
            self.sendtext(item)

    def get_blog_post(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find('div', class_='single-post single-view')
        title = soup.find('a', href=url)
        paragraphs = results.find_all('p')
        blog_post = []
        for paragraph in paragraphs:
            blog_post.append(paragraph.text)
        blog_post.insert(0, title.text.upper())
        return blog_post

    # Uses a starting url to exploit the pages Random post button that always gives a random post. Bad practice but works
    def get_random_url(self):
        starting_page = requests.get(
            "https://seths.blog/2020/07/fake-deadlines/")
        soup = BeautifulSoup(starting_page.content, 'html.parser')

        ## Snajdipapa ##
        random_url = soup.find(
            'div', class_='random-post').find('form').get('action')
        return random_url

    def run(self):
        bot.sendtext("================================")
        bot.sendtext(
            f"Good morning Krisz, today is: {self.DotW}. {self.today}!")
        bot.sendtext(f"The temperature in Ealing is: {bot.get_weather()}")
        bot.sendtext("Here is a Blog post:")
        post = self.get_blog_post(self.url)
        bot.send_blogpost(post)
        bot.sendtext("Have a good day!")
        bot.sendtext("================================")

    def day_of_the_week(self):
        days = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
        dayNumber = date.weekday(self.today)
        return days[dayNumber]

    def get_weather(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = config('CITY')
        api_key = config('WEATHER_API')
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            # store the value corresponding
            # to the "temp" key of y
            current_temperature = str(round(y["temp"] - 273.15, 2))
            z = x["weather"]
            weather_description = str(z[0]["description"])
            weather_report = current_temperature + \
                "°C" + "\n" + "Weather description = " + weather_description
            return weather_report


bot = Chadbot()
bot.run()
