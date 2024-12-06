#pip install telepot opencv-python-headless requests
import telepot
from picamera2 import Picamera2

camera = Picamera2()
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = telepot.Bot(bot_token)

def handle(msg):
    if msg['text'] == '/take_photo':
        camera.start_preview()
        time.sleep(2)
        camera.capture('photo.jpg')
        camera.stop_preview()
        bot.sendPhoto(msg['chat']['id'], open('photo.jpg', 'rb'))
    return msg

def main():
    bot.message_loop(handle)

if _name_ == '_main_':
    main()