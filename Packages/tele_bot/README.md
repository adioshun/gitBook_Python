https://swlock.blogspot.com/2019/04/raspberry-pi-creating-telegram-bot.html


```python 
import telegram
bot = telegram.Bot(token="") 
bot.sendMessage(chat_id = "", text = "hi") 
```


```python 
#-*- coding: utf-8 -*-

import time
import telepot
from telepot.loop import MessageLoop
 
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print("content_type:",content_type)
    #print("chat_type:",chat_type)
    #print("chat_id:",chat_id)
 
    if content_type == 'text':
        if msg['text'].upper() == 'hello':
            bot.sendMessage(chat_id, 'good morning')
        elif msg['text'] == '/start':
            pass
        else:
            bot.sendMessage(chat_id, '지원하지 않는 기능입니다 :)')
 
 
TOKEN = ''  # 텔레그램으로부터 받은 Bot 토큰

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()

print ('Listening ...')
while True:
    time.sleep(1000)
```
