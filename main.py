import queue
import random
import telegram

from konlpy.tag import Mecab
from telegram.ext import Updater, MessageHandler, Filters
#from emoji import emojize

# api_key, bot, chat_id setting
api_key = '5333196879:AAHyqMVrtXCS3DDQhnjVpgVrDf_GX5NxJ3Q' # minju's api_key
bot = telegram.Bot(token=api_key)
chat_id = 5385808815

# updater
updater = Updater(token='5333196879:AAHyqMVrtXCS3DDQhnjVpgVrDf_GX5NxJ3Q')
dispatcher = updater.dispatcher
updater.start_polling()


''' 선언 '''
# queue 선언
q = queue.Queue

# 민주의 답장 리스트 생성
alswnReq = []

# word update
anjgo = ['뭐해', '모해', '머해', '모행', '머행', '뭐행', 'ㅁㅎ'] # 뭐해?

# mecab 선언
mecab = Mecab()

#민주의 상태 리스트
statuslist = ['게임', '과제', '공부', '영화', '넷플릭스', '유원']

# 파이썬 구조체 선언
class Status:
    status: str = random.choice(statuslist)
    index: int = statuslist.index(status)
    hogamdo: int = None
# 구조체 초기값 재선언 -> main.py와 똑같은 값 -> 완료
minju = Status()
minju.status = minju.status
minju.index = minju.index

# 민주의 상태를 재설정하는 함수
def minjuStatus():
    print("구조체 설정 완료")
    minju = Status()
    minju.status = random.choice(statuslist)
    minju.index = statuslist.index(minju.status)
# 민주 호감도 초기설정 -> 완료
minju.hogamdo = 0

# 같은 질문을 여러번 하는지 체크하는 리스트
checkWord = [] # queue 의 형태로 구현
# index = 2 가 가장 최신

# 답장 횟수를 체크하는 변수
countQuestion = 0

''' 여기까지 한번만 실행 '''

# 0 ~ 5점을 랜덤하게 호감도를 부여
def plusHogamdo():
    minju.hogamdo += random.randint(0,5)

def minusHogamdo():
    minju.hogamdo -= random.randint(5,10)

def pushWordList(word):
    checkWord.append(word)

def popWordList(word):
    checkWord[0] = checkWord[1]
    checkWord[1] = checkWord[2]


''' 질문에 따른 분기 '''
print(f" 민주의 현재 상태 : status = {minju.status}, index = {minju.index}") ## 완료

# 질문에 따른 분기
def question(text): # 질문
    print("[질문 진입]")
    global countQuestion

    countQuestion += 1
    if(countQuestion == 3):
        popWordList() # 3개의 질문마다 가장 처음에 했던 질문 제거
        countQuestion = 0

    if('갈래' in text):
        pass
    if('할래' in text):
        pass
    if('볼래' in text):
        pass

    # ~해 알고리즘 완성
    if('해' in text): # ~해?
        print("[~해]")
        #status = mj.isStatus() # 민주의 현재 상태를 불러옴

        # 뭐 해?
        wordflag = 1
        if('뭐' in text):
            for i in checkWord: # 큐에 저장된 내가한 질문중 했던말이 있다면 (최대 3회)
                if( i == '뭐해' ): # 이전에 뭐해라고 했던적이 있으면
                    wordflag = 0 #
            # 민주 답장 추가
            if(wordflag): # 이전에 내가 했던말이 아니라면 수행
                if( minju.index == 5): # 내가 나왔으면
                    alswnReq.append('너생각')
                    plusHogamdo()

                elif( minju.index >= 0 and minju.index <= 2 ): # 활동을 하는 명사
                    alswnReq.append(minju.status)
                    alswnReq.append('하는중') # ~ 하는중
                    plusHogamdo()

                    print(minju.hogamdo)

                elif( minju.index >= 3 and minju.index <= 4 ): # 시청을 하는 명사
                    alswnReq.append(minju.status)
                    alswnReq.append('보는중') # ~ 보는중
                    plusHogamdo()

                # 내가 한 질문들을 큐에 저장.
                pushWordList('뭐해')

            else: # 만약 이전에 내가 했던 말이라면
                alswnReq.append('아까 말 했잖아')

        # 과제 해?
        elif('과제' in text):
            pass

            '''
            wordIndex = [ index for index in statuslist if( index in text )]
            print(f"{wordIndex} 포함됨")
            #print(f"{random.choice(statuslist)} 하는중!")
            '''

    ''' 민주의 답장 알고리즘 종료 '''

def notQuestion(): # 질문아님
    print('질문ㄴㄴ')

''' 질문일때의 조건식 '''
'''
def hae():
    pass

def halrae():
    pass

def bolrae():
    pass

def galrae():
    pass
'''

''' 질문이 아닐때의 조건식 '''


''' 메인로직 '''

# main logic
def main():
    def handler(update, context):
        text = update.message.text
        # 형태소 분석기
        ### 명사만 추출해야 함 ### 제일 중요!!!!!!!
        MecabText = mecab.nouns(text)

        print(f"명사 : {MecabText}")

        # 로직 시작 #
        if '?' in text: # 질문일때
            question(text) # 질문으로 분기
        else: # 질문 아닐때
            notQuestion(text) # 질문 아님으로 분기


        # 미래형

        # 과거형

        # 뭐해?


        # 민주의 답장
        alswnSend = ''.join(alswnReq)
        bot.send_message(chat_id=chat_id, text=alswnSend)
        # 민주가 답장하면 리스트 클리어
        alswnReq.clear()
        bot.stopPoll()
# handler setting
    echo_handler = MessageHandler(Filters.text, handler)
    dispatcher.add_handler(echo_handler)

if __name__ == '__main__':
    main()
