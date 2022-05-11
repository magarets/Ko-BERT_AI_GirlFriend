import telegram
#import pymysql
from konlpy.tag import Mecab
from telegram.ext import Updater, MessageHandler, Filters

#from emoji import emojize

# api_key, bot, chat_id setting
api_key = '5249899073:AAHz_FcHjRqALlBzNGw-Ed_lyJMkvOJA-Mc' # minju's api_key
bot = telegram.Bot(token=api_key)
chat_id = 5385808815

# updater
updater = Updater(token='5249899073:AAHz_FcHjRqALlBzNGw-Ed_lyJMkvOJA-Mc')
dispatcher = updater.dispatcher
updater.start_polling()

# 민주의 답장 리스트 생성
alswnReq = []

# word update
anjgo = ['뭐해', '모해', '머해', '모행', '머행', '뭐행', 'ㅁㅎ'] # 뭐해?

# 민주 문장에 단어추가 (문장완성하는 곳)
def mohae():
    alswnReq.append('너생각')

# mecab 선언
mecab = Mecab()
# logic
def handler(update, context):
    text = update.message.text
    MecabText = mecab.pos(text)
    print(MecabText)

    # 미래형

    # 과거형

    # 뭐해?
    for t in anjgo: # 비슷한 의미를 지닌 단어를 단어리스트에서 검색
        if t in text:
            mohae()
            alswnReq.append('ㅎㅎ')

    # 민주의 답장
    alswnSend = ''.join(alswnReq)
    bot.send_message(chat_id=chat_id, text=alswnSend)
    # 민주가 답장하면 리스트 클리어
    alswnReq.clear()
# handler setting
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)