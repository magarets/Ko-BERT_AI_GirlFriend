'''
used {
- KcELECTRA
}
'''

import pandas as pd
import streamlit as st
import numpy as np
from numpy import dot
from numpy.linalg import norm

import string
import openpyxl
import operator
import tensorflow as tf
from transformers import TFBertForNextSentencePrediction
from transformers import AutoTokenizer

from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher
from konlpy.tag import Mecab

# 감성파일데이터 파일 로드
df = pd.read_excel('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/train_data.xlsx')
# 모델 불러오기
model = AutoTokenizer.from_pretrained("beomi/KcELECTRA-base")

ls = 0.90
text = '창 밖을 보는 고양이'
text2 = '창 밖을 보는 강아지'
# 텍스트 벡터화
embedding = model.encode(text)
embedding2 = model.encode(text2)

print(f'score: {dot(embedding, embedding2) / (norm(embedding) * norm(embedding2))}')
'''
for i in range(150 - len(embedding)):
    embedding.append(0)
'''

'''
# 전체 데이터에서 일치율 구하기
max = 0
for index, data in enumerate(df['Embedding']):
    # str 2 list
    myList_a = data.split(',')
    myList = list(map(int, myList_a))
    score = dot(embedding, myList) / (norm(embedding) * norm(myList))

    if(score > ls):
        if( max < score ):
            max = score
            point = index


print("test score")
print(f"{max}, {df.loc[point, 'Sentence']}, {df.loc[point, 'Emotion']}")

'''

#print(dot(embedding, embedding2) / (norm(embedding) * norm(embedding2)))
# 0 -> [2, 11495, 14524, 4012, 1470, 8008, 3]
# 안녕하세요 저는 민주입니다. -> [2, 18841, 8479, 10952, 8019, 8080, 18, 3]
# 안녕하세요 저는 성유원입니다 -> [2, 18841, 8479, 10952, 2062, 4266, 4195, 8080, 18, 3]

# 인코딩데이터를 엑셀 데이터로 저장
#df['embedding'] = df['user'].map(lambda x: list(model.encode(x)))

# 시퀀스 투 벡터 데이터베이스 저장
#df.to_csv('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/traindata.csv', index=False)
