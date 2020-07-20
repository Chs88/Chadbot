import requests


class Chadbot:
    def __init__(self):
        self.name = "Chadbot"

    def sendtext(self, bot_message):
        bot_token = '1340709229:AAHEPXRY5yRQmCP_XPcVoyJ05lus0P-Ia7o'
        bot_chatID = '1249893195'
        send_text = 'https://api.telegram.org/bot' + bot_token + \
            '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)


bot = Chadbot()
