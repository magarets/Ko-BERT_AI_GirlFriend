'''
used {
- KcELECTRA
}
'''

import pandas as pd
import string
import openpyxl
import operator
import tensorflow as tf
from transformers import TFBertForNextSentencePrediction
from transformers import AutoTokenizer

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher

# 모델 불러오기
#model = SentenceTransformer('jhgan/ko-sroberta-multitask')

model = AutoTokenizer.from_pretrained("beomi/KcELECTRA-base")

# 데이터 파일 로드
df = pd.read_excel('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/Minju_word_data.xlsx')

# 인코딩
#df_encode = model.encode(df.loc[0, 'user'])
df_encode_1 = model.encode('안녕하세요 저는 민주입니다.')
df_encode_2 = model.encode('안녕하세요 저는 성유원입니다.')

print((df_encode_1, df_encode_2))
# 0 -> [2, 11495, 14524, 4012, 1470, 8008, 3]
# 안녕하세요 저는 민주입니다. -> [2, 18841, 8479, 10952, 8019, 8080, 18, 3]
# 안녕하세요 저는 성유원입니다 -> [2, 18841, 8479, 10952, 2062, 4266, 4195, 8080, 18, 3]



# 인코딩데이터를 엑셀 데이터로 저장
#df['embedding'] = df['user'].map(lambda x: list(model.encode(x)))

# 시퀀스 투 벡터 데이터베이스 저장
#df.to_csv('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/traindata.csv', index=False)