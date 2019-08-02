import requests
import json
import datetime, time 
import schedule
import telepot
import threading
from telepot.loop import MessageLoop

chat_id = 386055474
url = "https://api.ownthink.com/bot?appid=xiaosi&userid=user&spoken={}"
def chat(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
    if content_type == 'text':
        m = msg['text']
        if m == "一言":
            r = requests.get("http://api.guaqb.cn/v1/onesaid/").text
            return bot.sendMessage(chat_id, r)
        else:
            r = requests.get(url.format(m)).json()
            reply = r["data"]["info"]["text"]
        return bot.sendMessage(chat_id, reply)

	# response = msg['text']
	# if chat_id not in d:
	# 	mark = 1
	# 	d[chat_id] = mark
	# 	msg = "Welcome! Please type in the bus stop code to get the bus arriaval timings."+UserGuide
	# 	return reply(msg, chat_id)








def morning():
    msg = "早上好呀~今天也要继续努力(＾Ｕ＾)ノ~ＹＯ"      
#     # msg = "你很棒"
    return bot.sendMessage(chat_id, msg)

def night():
    msg = "早点睡，晚安安"
    return bot.sendMessage(chat_id, msg)

def thurs():
    msg = "今天练琴了吗😭，要上课了"
    return bot.sendMessage(chat_id, msg)

schedule.every().day.at("07:00").do(morning)
schedule.every().day.at("01:00").do(night)
schedule.every().thursday.do(thurs)



bot = telepot.Bot("823067212:AAGPNZY-sKw-Irhm-Nv8aY8rswbb_KUhn0s")
MessageLoop(bot, chat).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    schedule.run_pending()
    time.sleep(1)
