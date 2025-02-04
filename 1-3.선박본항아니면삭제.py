import pandas as pd

# xlsx 파일 경로
xlsx_file = '선박입출항현황(210401-230331).xlsx'

# xlsx 파일을 DataFrame으로 읽어오기
df = pd.read_excel(xlsx_file)

# 삭제할 패턴 리스트
invalid_patterns = [
    '1부두 01',
    '2부두 01',
    '2부두 02',
    '2부두 03',
    '3부두 01',
    '3부두 02',
    '4부두 01',
    '4부두 02',
    '5부두 01',
    '6부두 01',
    '6부두 02',
    '6부두 03',
    '6부두 04',
    '6부두 05',
    '7부두 01',
    '8부두 01',
    '8부두 02',
    '9부두 01',
    'SK1부두 11',
    'SK1부두 12',
    'SK2부두 01',
    'SK2부두 02',
    'SK3부두',
    'SK4부두',
    'SK5부두',
    'SK6부두',
    'SK7부두',
    'SK8부두',
    'SK부이 02',
    'SK부이 03',
    'UTT부두',
    '가스부두',
    '남화부두',
    '일반부두 01',
    '일반부두 02',
    '일반부두 03',
    '일반부두 04',
    '일반부두 05',
    '일반부두 06',
    '일반부두 07',
    '일반부두 08',
    '자동차부두 01',
    '자동차부두 02',
    '자동차부두 03',
    '염포부두 01',
    '염포부두 02',
    '염포부두 03'
]

#예시 - df = df[df.계선장소 != ']

df = df[df['계선장소'].isin(invalid_patterns) == True]

output_file = 'filtered_data.xlsx'
df.to_excel(output_file, index=False)

#