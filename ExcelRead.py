import pandas as pd
import string
import openpyxl
import operator

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher

'''
model = SentenceTransformer('jhgan/ko-sroberta-multitask')

sentence = ["안녕하세요?", "한국어 문장 임베딩을 위한 버트모델입니다."]
embeddings = model.encode(sentence)

print(embeddings)
''' # Sentence BERT 모델 벡터화


# 사용자 입력과 시나리오 데이터의 일치율 분석 
def compareWord(a_str, b_str):
    SequenceMatcher(None, a_str, b_str).ratio()
    match_rate = f'{SequenceMatcher(None, a_str, b_str).ratio() * 100:.1f}'
    return match_rate

userChatLog = [] # 사용자의 최대 3회의 채팅로그를 저장하는 리스트
minjuChatLog = [] # 인공지능의 채팅로그
Loop = 3 # 최대 n 번의 대화시나리오를 생성


# 데이터 읽어오기
df_minju = pd.read_excel('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/Minju_word_data.xlsx', usecols=[3], skiprows=[1])
df_user = pd.read_excel('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/Minju_word_data.xlsx', usecols=[2], skiprows=[1])
df_sinario = pd.read_excel('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/Minju_word_data.xlsx', usecols=[1], skiprows=[1])

# 테스트를 위한 앞 20개만 읽어오기
#df_user = df_user.head(20)

# 엑셀에서 추출한 사용자 발화를 문자열 변환
df_user = df_user.astype('str')

# 문자열로 바꾼 사용자 발화를 리스트로 변환
userDataList = df_user.values.tolist()
# 시나리오 데이터를 리스트로 변환
sinarioDataList = df_sinario.values.tolist()
# 민주의 데이터를 리스트로 변환
minjuDataList = df_minju.values.tolist()

# 사용자 입력받고, 공백제거
userInput = input("input : ")
userInput = ''.join(userInput)
userInput = userInput.replace(" ", "")

# 학습 데이터 일치율 %
# 80 이상이 적당한듯? 70은 다른시나리오에서도 검색됨
ld = 80

''' start '''

# 사용자 발화문 리스트에서 형태소 추출 후, 사용자 입력 데이터와 비교해서 시나리오 찾기
for index, data in enumerate(userDataList):
    compareData = ''.join(data)
    compareData = compareData.replace(" ", "") # 문자열 공백제거

#    print(compareData, " ")

    ''' 사용자 입력과 데이터의 일치율 비교 '''
    # 두 개의 문자열의 일치율을 구하기
    match_rate = float(compareWord(userInput, compareData))

    if(match_rate > ld):
        print(f"{index} {userInput}, {compareData} => {match_rate}%")
        print(f"시나리오 : {sinarioDataList[index]}")



'''
wb = openpyxl.Workbook()
wb.save('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/Minju_word_data.xlsx')
'''
