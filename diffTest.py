from difflib import SequenceMatcher
a_str = '니이름알려줘'
b_str = '너이름뭐야'
SequenceMatcher(None, a_str, b_str).ratio()

match_rate = f'{SequenceMatcher(None, a_str, b_str).ratio()*100:.1f}%'
print(match_rate)