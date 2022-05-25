import telegram
import asyncio  # 비동기 사용을 위한 asyncio 모듈

from konlpy.tag import Mecab
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

# 대화기록을 저장하는 리스트
userList = []

''' pingpong start '''

# URL, Token 생성
URL = ""  # 핑퐁 커스텀 API 사이트에서 링크
Authorization = ""  # 핑퐁 커스텀 API 사이트에서 인증 토큰

Ping = PingPong(URL, Authorization)  # 핑퐁 클래스 선언
sessionID = 'a'
async def Example():  # 비동기 사용을 위한 함수
    text = input(">>> ")  # 입력 받기
    data = await Ping.Pong("sessionid", text) # 자연스러운 대화를 위한 세션 아이디와
                                             # 전송할 텍스트
    print(data) # {"text": "안녕안녕입니다🖐", "image": None}

asyncio.run(Example())  # 비동기로 함수 실행
