"""
drinkdataex6.py : 대한민국 순위 확인
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# file_path = '/home/andybae/study/data/drinks.csv'
file_path = 'drinks.csv'
drinks = pd.read_csv(file_path)
print(drinks.info())
print(drinks['beer_servings'].head())

drinks['total_servings'] = drinks['beer_servings'] + drinks['wine_servings'] + drinks['spirit_servings'] # total_servings 이라는 컬럼 추가

drinks['alcohol_rate'] = drinks['total_litres_of_pure_alcohol'] / drinks['total_servings']
print(drinks.info()) 
drinks['alcohol_rate'] = drinks['alcohol_rate'].fillna(0) #fillna : null 값인 경우 0으로 변경
print(drinks.info())

# 순위 정보를 생성
country_with_rank = drinks[['country','alcohol_rate']] 
print(country_with_rank.head(10)) # 상위 10개 레코드 조회
country_with_rank = country_with_rank.sort_values(by=['alcohol_rate'], ascending=0)
print(country_with_rank.head(30))

# 국가별 순위 정보를 그래프로 시각화
country_list = country_with_rank.country.tolist() # country 칼럼만 리스트로 저장
x_pos = np.arange(len(country_list))  
rank = country_with_rank.alcohol_rate.tolist() # alcohol_rate 컬럼만 리스트로 저장, 막대그래프로 작성할 데이터

bar_list = plt.bar(x_pos, rank) #막대 그래프 그리기

bar_list[country_list.index("South Korea")].set_color('r')
plt.ylabel('alcohol rate')
plt.title('liquor drink rank by country')
plt.axis([0, 200, 0, 0.3]) # x,y 축 값의 범위

korea_rank = country_list.index("South Korea")
print(korea_rank)
korea_alc_rate = country_with_rank[country_with_rank['country'] == 'South Korea']['alcohol_rate'].values[0]
print(korea_alc_rate)

# -> 표시
plt.annotate('South Korea : ' + str(korea_rank + 1), xy=(korea_rank, korea_alc_rate), xytext=(korea_rank + 10, korea_alc_rate + 0.05),\
             arrowprops=dict(facecolor='red', shrink = 0.05))
