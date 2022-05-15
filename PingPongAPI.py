from PingPongTool import PingPong  # 핑퐁툴 모듈 임포트
import asyncio  # 비동기 사용을 위한 asyncio 모듈

URL = "이곳에 커스텀 API 링크를 넣으세요"  # 핑퐁 커스텀 API 사이트에서 링크
Authorization = "이곳에 인증 토큰을 넣으세요"  # 핑퐁 커스텀 API 사이트에서 인증 토큰

Ping = PingPong(URL, Authorization)  # 핑퐁 클래스 선언

async def Example():  # 비동기 사용을 위한 함수
    text = input(">>> ")  # 입력 받기
    data = await Ping.Pong("Example", text)  # 자연스러운 대화를 위한 세션 아이디와
                                             # 전송할 텍스트
    print(data) # {"text": "안녕안녕입니다🖐", "image": None}

asyncio.run(Example())  # 비동기로 함수 실행