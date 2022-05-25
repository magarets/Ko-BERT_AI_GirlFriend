## start chatting ##
# 디스코드 봇 토큰 : 
import re
import random
import PingPongWr

from konlpy.tag import Okt
from sentence_transformers import SentenceTransformer, util
from discord.ext import commands



model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

# open Okt
okt = Okt()

# creat list
minjuReq = ['왜 아까했던말 또 해?', '뭐야.. 왜 같은말 자꾸 해', '그건 아까 말했잖아', '아까 말한거잖아!!']
userInputLog = []
result = []
vectors_2 = []
sim_list = []

# similarities score
score = 0.7

# bot 생성
bot = commands.Bot(command_prefix='>')

#  ping-pong setting
sessionID = ''
url = "" + 'sessionid'  # 핑퐁빌더 Custom API URL
pingpong_token = ""  # 핑퐁빌더 Custom API Token

Ping = PingPongWr.Connect(url, pingpong_token)  # 핑퐁 모듈 클래스 선언
text = 'abcedfghijklmn'


# start discord
# 비동기 함수로 실행
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # 사용자로부터 입력이 들어온다면
    if not message.content.startswith(text):
        # 사용자 발화를 str로 변환
        str_text = ' '.join((message.content.split(" ")))

        # print user-message
        print(str_text)

        ''' start logic '''

        # input user's chat
        Input = str_text

        # 데이터 정규화
        normal_data = okt.normalize(Input)

        # 불용어 제거 ㄱ ~ ㅎ
        delete_stopword_data = re.sub('[ㄱ-ㅎ]', '', normal_data)

        # 정제된 문장을 로그에 추가 (이건 사실 필요없음)
        userInputLog.append(' '.join(delete_stopword_data.split(' ')))

        print(f"정제된 문장 : {userInputLog}")

        # 사용자 입력을 diff로 검사 (단순 문자열 일치율)
        # result = list(map(lambda x: SequenceMatcher(None, Input, x).ratio()*100, userInputLog))

        # 입력 벡터화
        vectors = model.encode(delete_stopword_data)  # encode sentences into vectors
        print(vectors)
        # 입력 벡터화값 리스트에 추가
        vectors_2.append(vectors)

        # 벡터값의 유사도 검사
        similarities = list(map(lambda x: util.cos_sim(vectors, x), vectors_2))

        ''' end logic '''
        # 유저의 채팅로그에서 비슷한 벡터 유사도가 검출되는지 확인
        # True : 비슷한 문장 없음
        # Flase : 비슷한 문장 있음
        flag = True

        # 벡터 리스트에서 입력 문장의 유사도 검출
        if(len(similarities) != 1):
            for data in range(0, len(similarities)-1):
                print(f"유사도 : {similarities[data]} > {score}")
                flag = False if float(similarities[data]) > score else True

        # 최근 3턴 이내에 같은 문장이 없으면 사용자 발화문 전송
        if( flag ):
            return_data = await Ping.Pong(session_id ="Example", text = str_text, topic = True, image = True, dialog = True)

        # 같은 문장이 있으면
        else:
            Req = random.choice(minjuReq)
            return_data = {'text': Req}
            print("최근 3턴동안 비슷한 문장을 했음")

        # 최대 3턴의 최신 로그만 저장. 해당 리스트는 오른쪽으로 자람
        if (len(vectors_2) > 2):
            vectors_2.pop(0)
            userInputLog.pop(0)

        ''' 사용자 발화문 종료 '''
        print("-"*20)

        # discord에 response 전송 -> text만 추출
        await message.channel.send(f"{return_data['text']}")

print('start')
# discord bot's token
bot.run('')
