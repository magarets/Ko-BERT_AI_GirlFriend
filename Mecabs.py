from konlpy.tag import Mecab

mecab = Mecab()
data = mecab.pos("지금 뭐해?")

for dataList in data:
    print(dataList)
print("")
for dataList in data:
    if( 'MAG' in dataList ): # 시간추출
        print(dataList)

