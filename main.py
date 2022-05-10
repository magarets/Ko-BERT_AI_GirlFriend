import telegram

api_key = '5249899073:AAHz_FcHjRqALlBzNGw-Ed_lyJMkvOJA-Mc' # minju's api_key

bot = telegram.Bot(token=api_key)

#chat_id = bot.get_updates()[-1].message.chat_id # chat_id 추출
chat_id = 5385808815 # 민주와 나의 연결고리

bot.sendMessage(chat_id=chat_id, text="유원아 머해?")