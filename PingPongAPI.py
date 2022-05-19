import requests
from PingPongTool import PingPong  # 핑퐁툴 모듈 임포트
import asyncio  # 비동기 사용을 위한 asyncio 모듈

URL = "https://builder.pingpong.us/api/builder/627c7214e4b0d7787e92b6fe/integration/v0.2/custom/{sessionId}"  # 핑퐁 커스텀 API 사이트에서 링크
Authorization = "Basic a2V5OjQ0ZDdjN2ZmYTJkYTFmNTA2Zjg4ODhlMjEyYzk3MDg3"  # 핑퐁 커스텀 API 사이트에서 인증 토큰

Ping = PingPong(URL, Authorization)  # 핑퐁 클래스 선언
sessionID = 'a'
async def Example():  # 비동기 사용을 위한 함수
    text = input(">>> ")  # 입력 받기
    data = await Ping.Pong("sessionid", text) # 자연스러운 대화를 위한 세션 아이디와
                                             # 전송할 텍스트
    print(data) # {"text": "안녕안녕입니다🖐", "image": None}

asyncio.run(Example())  # 비동기로 함수 실행
