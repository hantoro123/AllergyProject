import pymysql, json, requests, os
import pandas as pd
from math import sqrt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 유사도 계산 #
def sim_person(data, allergy1, allergy2):
    sumX=0
    sumY=0
    sumPowX=0
    sumPowY=0
    sumXY=0
    count=0

    for i in data[allergy1].keys():
        if i in data[allergy2].keys():
            sumX+=data[allergy1][i]
            sumY+=data[allergy2][i]
            sumPowX+=pow(data[allergy1][i],2)
            sumPowY+=pow(data[allergy2][i],2)
            sumXY+=data[allergy1][i]*data[allergy2][i]
            count+=1

    return ( sumXY- ((sumX*sumY)/count) )/ sqrt( (sumPowX - (pow(sumX,2) / count)) * (sumPowY - (pow(sumY,2)/count)))


# 최대 유사도 구하기 #
def top_match(data, allergy, index=3, sim_function=sim_person):
    li=[]
    for i in data:
        if allergy != i:
            li.append((sim_function(data,allergy,i), i))
    li.sort()
    li.reverse()

    return li[:index]


# DB 연결 #
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='2017018023',
                       db='allergydb',
                       charset='utf8')
cur = conn.cursor()

# Mysql에서 DATA 읽기 (전처리 포함) #
cur.execute("""SELECT prdlstReportNo,prdlstNm FROM searchapp_product""")
proData = cur.fetchall()
print(proData[0])        # product data 확인용

cur.execute("""SELECT gender,older,allergy,prdlstReportNo,prdlstNm,rating FROM searchapp_userdata""")
choData = cur.fetchall()
print(choData[0])         # user data 확인용

# 형식 변환 #
pdProData = pd.DataFrame(proData)
pdChoData = pd.DataFrame(choData)

# 병합 #
merge_data = pd.concat([pdProData, pdChoData], join='inner')
print(merge_data)

conn.close()