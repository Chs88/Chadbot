import requests
from bs4 import BeautifulSoup


class Chadbot:
    def __init__(self):
        self.name = "Chadbot"
        self.url = 'https://seths.blog/2018/09/the-solution-to-stalled/'

    def sendtext(self, bot_message):
        bot_token = '1340709229:AAHEPXRY5yRQmCP_XPcVoyJ05lus0P-Ia7o'
        bot_chatID = '1249893195'
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
        blog_post.insert(0, "Title: " + title.text)
        return blog_post


bot = Chadbot()
bot.send_blogpost(bot.get_blog_post(bot.url))
