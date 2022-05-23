import os,telebot,random
#API_KEY = '5371447772:AAEdCS1uatFPrNxp9YdiknV-PLLCDSdQN4s'
TOKEN = "5371447772:AAEdCS1uatFPrNxp9YdiknV-PLLCDSdQN4s"
ai = telebot.TeleBot(TOKEN)
@ai.message_handler(commands=['gg'])
def reallo(message):
  ai.send_message(message.chat.id,"hi")
  #ai.send_video(chat_id='receiver chat id', video=open(file_name, 'rb')), timeout=10000)
  lists = random.choice(os.listdir("/root/orkspace/"))
  futo = open("/root/orkspace/2035690.jpg",'rb')
  ai.send_photo(message.chat.id,"hi",futo)

ai.polling()