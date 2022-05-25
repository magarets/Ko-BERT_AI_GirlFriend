import telegram
import asyncio  # 비동기 사용을 위한 asyncio 모듈

from konlpy.tag import Mecab
from telegram.ext import Updater, MessageHandler, Filters
from PingPongTool import PingPong  # 핑퐁툴 모듈 임포트
#from emoji import emojize

# api_key, bot, chat_id setting
api_key = '5333196879:AAHyqMVrtXCS3DDQhnjVpgVrDf_GX5NxJ3Q' # minju's api_key
bot = telegram.Bot(token=api_key)
chat_id = 5385808815

# updater
updater = Updater(token='5333196879:AAHyqMVrtXCS3DDQhnjVpgVrDf_GX5NxJ3Q')
dispatcher = updater.dispatcher
updater.start_polling()

# 핑퐁 api 설정
URL = "https://builder.pingpong.us/api/builder/627c7214e4b0d7787e92b6fe/integration/v0.2/custom/{sessionId}"  # 핑퐁 커스텀 API 사이트에서 링크
Authorization = "Basic a2V5OjQ0ZDdjN2ZmYTJkYTFmNTA2Zjg4ODhlMjEyYzk3MDg3"  # 핑퐁 커스텀 API 사이트에서 인증 토큰

# 핑퐁 클래스 선언
Ping = PingPong(URL, Authorization)
sessionID = 'a'

# Session ID
sessionID = 'a'

# main logic
'''
async def Example(text):
    # 핑퐁 Response
    data = await Ping.Pong("sessionid", text)
    print('test!!')
    print(data)

    return data
'''
''' 핑퐁 함수
def requestData(data):
    print(f'message: {data}')
    req = await Ping.Pong('sessionid', data)
    print(req)
'''

# 텔레그램
def handler(update, context):
    # request
    print("start!")
    text = update.message.text

    print(f"res: {text}")
#    await requestData(text)

    # response
    bot.send_message(chat_id=chat_id, text=text)
    print(f"user: {text}")

#        bot.stopPoll()
# handler setting
print("start telegram")
echo_handler = MessageHandler(Filters.text, handler)
print("set echo_handler")
dispatcher.add_handler(echo_handler)
print("set dispatcher")
print("hi")



"""
import telegram
import asyncio  # 비동기 사용을 위한 asyncio 모듈

from konlpy.tag import Mecab
from telegram.ext import Updater, MessageHandler, Filters
from PingPongTool import PingPong  # 핑퐁툴 모듈 임포트
#from emoji import emojize

# api_key, bot, chat_id setting
api_key = '5333196879:AAHyqMVrtXCS3DDQhnjVpgVrDf_GX5NxJ3Q' # minju's api_key
bot = telegram.Bot(token=api_key)
chat_id = 5385808815

# updater
updater = Updater(token='5333196879:AAHyqMVrtXCS3DDQhnjVpgVrDf_GX5NxJ3Q')
dispatcher = updater.dispatcher
updater.start_polling()

# 핑퐁 api 설정
URL = "https://builder.pingpong.us/api/builder/627c7214e4b0d7787e92b6fe/integration/v0.2/custom/{sessionId}"  # 핑퐁 커스텀 API 사이트에서 링크
Authorization = "Basic a2V5OjQ0ZDdjN2ZmYTJkYTFmNTA2Zjg4ODhlMjEyYzk3MDg3"  # 핑퐁 커스텀 API 사이트에서 인증 토큰

# 핑퐁 클래스 선언
Ping = PingPong(URL, Authorization)

# Session ID
sessionID = 'a'

# main logic
'''
async def Example(text):
    # 핑퐁 Response
    data = await Ping.Pong("sessionid", text)
    print('test!!')
    print(data)

    return data
'''
''' 핑퐁 함수
async def requestData(data):
    print(f'message: {data}')
    req = await Ping.Pong('sessionid', data)
    print(req)
'''

# 텔레그램
def handler(update, context):
    # request
    print("start!")
    text = update.message.text

#    await requestData(text)

    # response
    bot.send_message(chat_id=chat_id, text=text)
    print(f"user: {text}")

#        bot.stopPoll()
# handler setting
print("start telegram")
echo_handler = MessageHandler(Filters.text, handler)
print("set echo_handler")
dispatcher.add_handler(echo_handler)
print("set dispatcher")
print("hi")
"""