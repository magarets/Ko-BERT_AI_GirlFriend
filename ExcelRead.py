import pandas as pd
import string
import openpyxl
import operator

from difflib import SequenceMatcher

# 사용자 입력과 시나리오 데이터의 일치율 분석
def compareWord(a_str, b_str):
    SequenceMatcher(None, a_str, b_str).ratio()
    match_rate = f'{SequenceMatcher(None, a_str, b_str).ratio() * 100:.1f}'
    return match_rate



# 데이터 읽어오기
df_user = pd.read_excel('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/Minju_word_data.xlsx', usecols=[2], skiprows=[1])
df_sinario = pd.read_excel('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/Minju_word_data.xlsx', usecols=[1], skiprows=[1])

# 테스트를 위한 앞 20개만 읽어오기
#df_user = df_user.head(20)

# 엑셀에서 추출한 사용자 발화를 문자열 변환
df_user = df_user.astype('str')

# 문자열로 바꾼 사용자 발화를 리스트로 변환
userDataList = df_user.values.tolist()
# 사나리오 데이터를 리스트로 변환
sinarioDataList = df_sinario.values.tolist()

# 사용자 입력받고, 공백제거
userInput = input("input : ")
userInput = ''.join(userInput)
userInput = userInput.replace(" ", "")

# 학습 데이터 일치율 %
ld = 80

# 사용자 발화문 리스트에서 형태소 추출 후, 사용자 입력 데이터와 비교해서 시나리오 찾기
for index, data in enumerate(userDataList):
    compareData = ''.join(data)
    compareData = compareData.replace(" ", "") # 문자열 공백제거

#    print(compareData, " ")

    ''' 사용자 입력과 데이터의 일치율 비교문 '''
    # 두 개의 문자열의 일치율을 구하기
    match_rate = float(compareWord(userInput, compareData))

    if(match_rate > ld):
        print(f"{index} {userInput}, {compareData} => {match_rate}")
        print(f"시나리오 : {sinarioDataList[index]}")

'''
wb = openpyxl.Workbook()
wb.save('/Users/itsjustyuwon/Desktop/Desktop/desktop/opensource/Telegram_GF/data/Minju_word_data.xlsx')
'''
