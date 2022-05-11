import telegram
import logic
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

# mecab 선언
mecab = Mecab()
''' 여기까지 한번만 설정하면 됨 '''


''' 문장완성 식 시작 '''
# 민주 문장에 단어추가 (문장완성하는 곳)
def mohae():
    alswnReq.append('너생각')

''' 질문에 따른 분기 '''


# main logic
def main():
    def handler(update, context):
        text = update.message.text
        # 형태소 분석기
        #MecabText = mecab.pos(text)

        # 로직 시작 #
        if '?' in text: # 질문일때
            print('테스트. 질문임')
            question()
        else: # 질문 아닐때
            notQuestion()


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

if __name__ == '__main__':
    main()
