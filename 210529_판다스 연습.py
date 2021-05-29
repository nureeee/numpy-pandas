import pandas as pd
import numpy as np

string_data = pd.Series(['a', 'b', np.nan, 'c'])
string_data
string_data.isnull()

string_data[0] = None
from numpy import nan as NA
data = pd.Series([1, NA, 3.5, NA, 7])
data.dropna()
data[data.notnull()]

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()

data.dropna(how='all')
data[4] = NA
data.dropna(axis=1, how='all')

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
df

df.dropna()
##행의 값의 개수가 2가 넘는 행만 모으기
df.dropna(thresh=2)
#누락된 값을 0으로 채우기
df.fillna(0) 
## None의 원하는 값을 넣음
df.fillna({1: 0.5, 2:0})
## inplace True는 원본 값을 수정??
_ = df.fillna(0, inplace=True)

df = pd.DataFrame(np.random.randn(6, 3))
df.loc[2:, 1]=NA
df.iloc[4:, 2] = NA
df.fillna(method='ffill')

data = pd.DataFrame({'k1': ['one', 'two']*3 + ['two'], 'k2': [1, 1, 2, 3, 3, 4, 4]})
## 각 로우가 중복인지 아닌지 알려줌
data.duplicated()
##duplicated 배열이 False인 데이터프레임을 반환한다
data.drop_duplicates()
data['v1'] = range(7)
##k1을 기준으로 중복되는 값을 거른다
data.drop_duplicates(['k1'])

## 이해가 안된다 ㅠㅠ
data.drop_duplicates(['k2'], keep='last')

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
cats
cats.codes

cats.categories
pd.value_counts(cats)

mnames = ['id', 'title', 'genres']



