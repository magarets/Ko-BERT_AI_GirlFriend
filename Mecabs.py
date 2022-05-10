from konlpy.tag import Mecab

mecab = Mecab()
data = mecab.pos("민주야 뭐해? 내일 영화보러갈래?")

for dataList in data:
    print(dataList)

