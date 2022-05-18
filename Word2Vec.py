import pandas as pd
import matplotlib.pyplot as plt
import gensim

from konlpy.tag import Okt
from gensim.models.word2vec import Word2Vec

#train_data = pd.read_table('')

pd_data = pd.read_csv("/Users/itsjustyuwon/Desktop/traindata.csv", usecols=[2])

train_data = pd_data.values.tolist()

stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']
okt = Okt()
tokenized_data = []

for index, data in enumerate(train_data):
    list2str = ''.join(data)
    train_data[index] = list2str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")

    print(train_data[index])
    tokenized_sentence = okt.morphs(train_data[index], stem=True)  # 토큰화
    stopwords_removed_sentence = [word for word in tokenized_sentence if not word in stopwords]  # 불용어 제거
    tokenized_data.append(stopwords_removed_sentence)

# 모델 학습
model = Word2Vec(sentences=tokenized_data, vector_size=100, window=5, min_count=3, workers=4, sg=0)

# 생성된 벡터 저장
model.save('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/word2vec.model')

model = Word2Vec.load('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/word2vec.model')
#word2vec_model = gensim.models.KeyedVectors.load_word2vec_format(model)
str_a = '뭐해'

print(model.wv.similarity('ㄴㄴ', 'ㅇㅇ'))

