'''
import random
# main.py #
import MJstatus as mj
from dataclasses import dataclass # 파이썬 구조체
import random
import queue

# queue 선언
q = queue.Queue

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

# 민주의 대답 리스트
alswnAnswer = []

# 같은 질문을 여러번 하는지 체크하는 리스트
checkWord = []

# 답장 횟수를 체크하는 변수
global countQuestion

print(f" 민주의 현재 상태 : status = {minju.status}, index = {minju.index}") ## 완료
## 구조체 완료

''' 여기까지 한번만 실행 '''
# 0 ~ 5점을 랜덤하게 호감도를 부여
def plusHogamdo():
    minju.hogamdo += random.randint(0,5)

# 질문에 따른 분기
def question(text): # 질문
    print("[질문 진입]")
    countQuestion += 1
    if(countQuestion == 3):
        q.get() # 3개의 질문마다 가장 처음에 했던 질문 제거
        countQuestion = 0

    if('갈래' in text):
        pass
    if('할래' in text):
        pass
    if('볼래' in text):
        pass

    if('해' in text): # ~해?
        print("[~해]")
        #status = mj.isStatus() # 민주의 현재 상태를 불러옴

        # 뭐 해?
        wordflag = 1
        if('뭐' in text):
            for i in q: # 큐에 저장된 내가한 질문중 했던말이 있다면 (최대 3회)
                if( i == '뭐해' ): # 이전에 뭐해라고 했던적이 있으면
                    wordflag = 0 #
            # 민주 답장 추가
            if(wordflag): # 이전에 내가 했던말이 아니라면 수행
                if( minju.index == 5): # 내가 나왔으면
                    alswnAnswer.append('너생각')
                    plusHogamdo()

                elif( minju.index >= 0 and minju.index <= 2 ): # 활동을 하는 명사
                    alswnAnswer.append(minju.status)
                    alswnAnswer.append('하는중') # ~ 하는중
                    plusHogamdo()

                    print(minju.hogamdo)

                elif( minju.index >= 3 and minju.index <= 4 ): # 시청을 하는 명사
                    alswnAnswer.append(minju.status)
                    alswnAnswer.append('보는중') # ~ 보는중
                    plusHogamdo()

                # 내가 한 질문들을 큐에 저장.
                q.put('뭐해')

            else: # 만약 이전에 내가 했던 말이라면
                alswnAnswer.append('아까 말 했잖아')

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

'''
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

'''