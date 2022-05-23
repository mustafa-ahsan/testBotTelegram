import os,telebot,random
#API_KEY = '5371447772:AAEdCS1uatFPrNxp9YdiknV-PLLCDSdQN4s'
TOKEN = "5371447772:AAEdCS1uatFPrNxp9YdiknV-PLLCDSdQN4s"
ai = telebot.TeleBot(TOKEN)
@ai.message_handler(commands=['start'])
def reallo(message):
  ai.send_message(message.chat.id,"هلا نورت")
  #ai.send_video(chat_id='receiver chat id', video=open(file_name, 'rb')), timeout=10000)
@ai.message_handler(commands=['gg',"مرحبا"])
def realloe(message):
  ai.send_message(message.chat.id,"مراحب")

ai.polling()
