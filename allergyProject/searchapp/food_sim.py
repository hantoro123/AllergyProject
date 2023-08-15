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


# 서로 다른 알레르기 간의 유사도 #
def getRecommendation (data, allergy, sim_function=sim_person):
    result = top_match(proAlData, allergy, len(data))

    simSum=0
    score=0
    li=[]
    score_dic={}
    sim_dic={}

    for sim, al in result:
        if sim < 0 : continue
        for product in data[al].keys():
            if data[al][product] == 0:
                score += sim * data[allergy][product]
                score_dic.setdefault(product,0)
                score_dic[product] += score

                sim_dic.setdefault(product, 0)
                sim_dic[product] += sim
            
            score = 0

    for key in score_dic:
        score_dic[key] = score_dic[key]/sim_dic[key]
        if score_dic[key] != 0:
            li.append((score_dic[key],key))

    li.sort()
    li.reverse()

    return li


# DB 연결 #
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='2017018023',
                       db='allergydb',
                       charset='utf8')
cur = conn.cursor()

# Mysql에서 DATA 읽기 (전처리 포함) #
cur.execute("""SELECT prdlstReportNo, rawmtrl FROM searchapp_product""")
proData = cur.fetchall()
# print(proData[0:2])                                             # product data 확인용                                          # user data 확인용

# 전처리 #
prdlstReportNo = []
rawmtrl = []

for row in proData:
    prdlstReportNo.append(row[0])
    rawmtrl.append(row[1])

# count vector로 만들어서 cosine similar 만들기 #
vectorizer = CountVectorizer()
food_vector = vectorizer.fit_transform(rawmtrl)
food_simi_cate = cosine_similarity(food_vector, food_vector)

print(food_simi_cate)
print("\n")

conn.close()