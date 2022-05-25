'''
KR-SBERT
'''

from sentence_transformers import SentenceTransformer, util

# 모델 로드
# 런타임: 평균 15~20초
model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')

# 발화문 -> 기준: 0번째 index
'''
sentence =          ['창 밖을 보는 고양이']
compareSentence =   ['커피를 마시는 고양이']
'''

while(1):
    # 사용자 입력
    sentence = input("First: ") # if input: q -> break
    compareSentence = input("Second: ")

    if(sentence == 'q'):
        break

    # 사용자 입력 벡터화
    vectors = model.encode(sentence) # encode sentences into vectors
    vectors_2 = model.encode(compareSentence)

    # 벡터값의 유사도 계산
    similarities = util.cos_sim(vectors, vectors_2) # compute similarity between sentence vectors

    #유사도
    print(similarities)