"""
drinkdataex4.py : 대륙별 tatal_litres_of_pure_alcohol을 시각화
"""

from matplotlib import container
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'drinks.csv'
drinks = pd.read_csv(file_path)

total_mean = drinks.total_litres_of_pure_alcohol.mean() # 대륙별 알콜 섭취량 평균
continent_mean = drinks.groupby('continent')['total_litres_of_pure_alcohol'].mean() # 대륙명 코드
continents = continent_mean.index.tolist()
continents.append('mean')
print(continents)

# 대륙별 평균
x_pos = np.arange(len(continents)) # 0 ~ continents 갯수
alcohol = continent_mean.tolist()
alcohol.append(total_mean) # 전체 평균
print(alcohol)

# 그래프 그리기
bar_list = plt.bar(x_pos, alcohol, align='center', alpha=0.5) # alpha는 투명도, 1이면 불투명
bar_list[len(continents) - 1].set_color('r') # 마지막 막대의 색을 red로 설정
plt.plot([0,6], [total_mean, total_mean], "k--") # 선그래프 설정 total_mean 값에 해당하는 부분에 선그래프 설정
plt.xticks(x_pos, continents) # x축 이름 설정

plt.ylabel('total_litres_of_pure_alcohol')
plt.xlabel('total_litres_of_pure_alcohol by Continent')

plt.show()
