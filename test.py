import telegram
import asyncio  # 비동기 사용을 위한 asyncio 모듈
import PingPongWr
from telegram.ext import Updater, MessageHandler, Filters
from PingPongTool import PingPong  # 핑퐁툴 모듈 임포트

# telegram api_key, bot, chat_id setting
api_key = '5333196879:AAHyqMVrtXCS3DDQhnjVpgVrDf_GX5NxJ3Q' # minju's api_key
bot = telegram.Bot(token=api_key)
chat_id = 5385808815

# telegram updater
updater = Updater(token='5333196879:AAHyqMVrtXCS3DDQhnjVpgVrDf_GX5NxJ3Q')
dispatcher = updater.dispatcher
updater.start_polling()

# URL, Token 생성
url = "https://builder.pingpong.us/api/builder/627c7214e4b0d7787e92b6fe/integration/v0.2/custom/{sessionId}"  # 핑퐁 커스텀 API 사이트에서 링크
Authorization = "Basic a2V5OjQ0ZDdjN2ZmYTJkYTFmNTA2Zjg4ODhlMjEyYzk3MDg3"  # 핑퐁 커스텀 API 사이트에서 인증 토큰

Ping = PingPongWr.Connect(url, Authorization)

sessionID = 'a'

@asyncio
async def handler(update, context):
    # request
    text = update.message.text

    print(text)
    res = await Ping.Pong(session_id ="sessionID", text = text, topic = True, image = True, dialog = True) # 핑퐁빌더 API에 Post 요청
    print(res)
    # response
    await bot.send_message(chat_id=chat_id, text=res)

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)