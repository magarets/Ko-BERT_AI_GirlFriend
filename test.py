import telegram
import asyncio  # 비동기 사용을 위한 asyncio 모듈
import PingPongWr
from telegram.ext import Updater, MessageHandler, Filters
from PingPongTool import PingPong  # 핑퐁툴 모듈 임포트

# telegram api_key, bot, chat_id setting
api_key = '' # minju's api_key
bot = telegram.Bot(token=api_key)
chat_id = 

# telegram updater
updater = Updater(token='')
dispatcher = updater.dispatcher
updater.start_polling()

# URL, Token 생성
url = ""  # 핑퐁 커스텀 API 사이트에서 링크
Authorization = ""  # 핑퐁 커스텀 API 사이트에서 인증 토큰

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
