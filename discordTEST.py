import re
from konlpy.tag import Okt
from sentence_transformers import SentenceTransformer, util
from difflib import SequenceMatcher
model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')


# open Okt
okt = Okt()

userInputLog = []
result = []
vectors_2 = []

while True:
    # input user's chat
    Input = input(">>> ")

    # 데이터 정규화
    normal_data = okt.normalize(Input)

    # 불용어 제거 ㄱ ~ ㅎ
    delete_stopword_data = re.sub('[ㄱ-ㅎ]', '', normal_data)

    # 정제된 문장을 로그에 추가 (이건 사실 필요없음)
    userInputLog.append(' '.join(delete_stopword_data.split(' ')))

    print(userInputLog)

    # 사용자 입력을 diff로 검사 (단순 문자열 일치율)
    #result = list(map(lambda x: SequenceMatcher(None, Input, x).ratio()*100, userInputLog))

    # 입력 벡터화
    vectors = model.encode(delete_stopword_data) # encode sentences into vectors

    # 입력 벡터화값 리스트에 추가
    vectors_2.append(vectors)

    # 벡터값의 유사도 검사
    similarities = list(map(lambda x: util.cos_sim(vectors, x), vectors_2))
    print(similarities)

    # 최대 3턴의 최신 로그만 저장. 해당 리스트는 오른쪽으로 자람
    if( len(vectors_2) > 2):
        vectors_2.pop(0)
        userInputLog.pop(0)

    if Input == 'q':
        break
