# 210531 월요일


import pandas as pd
import seaborn as sns

file_path = '/home/andybae/study/data/drinks.csv'

drinks = pd.read_csv(file_path) #

print("drinks.info():\n",drinks.info()) # 요약
print("drinks.describe():\n",drinks.describe()) # 통계를 상세 요약본

"""
corr : 상관계수
    pearson : 표준 상관계수
    kendall : 순위 상관계수
    spearman : 순위 상관계수
"""
# corr = drinks[['bear_servings', 'wine_servings']].corr(method='pearson')
# print(corr)


# 모든 컬럼의 상관계수
cols = ['bear_servings','spirit_servings','wine_servings','total_litres_of_pure_alcohol']
corr = drinks[cols].corr(method='pearson')
print(corr)

cols_view = ["beer","spirit","wing","alcohol"]
sns.set(font_scale=1.5)
hm = sns.heatmap(corr.values,cbar=True,annot=True,square=True,
                 fmt=".2f", annot_kws={'size':15},
                 yticklabels=cols_view,
                 xticklabels=cols_view)
