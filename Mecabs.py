from konlpy.tag import Mecab

mecab = Mecab()
data = mecab.pos("민주야 뭐해? 내일 영화 만들러 갈래?")

for dataList in data:
    print(dataList)
print("")
for dataList in data:
    if( 'MAG' in dataList ): # 시간추출
        print(dataList)

