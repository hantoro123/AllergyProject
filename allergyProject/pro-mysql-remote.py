# TQ : Test Query
from urllib.parse import unquote
import requests
import json
import pymysql

def Processed(dict, list):

    procData = []

        # if 'rnum' in list: procData.append(dict['rnum'])
    # else: procData.append('')

    if 'prdlstReportNo' in list: procData.append(dict['prdlstReportNo'].replace("\n", " "))
    else: procData.append('')

    if 'prdlstNm' in list: procData.append(dict['prdlstNm'].replace("\n", " "))
    else: procData.append('')

    # if 'productGb' in list: procData.append(dict['productGb'])
    # else: procData.append('')

    if 'prdkind' in list: procData.append(dict['prdkind'].replace("\n", " "))
    else: procData.append('')

    if 'rawmtrl' in list: procData.append(dict['rawmtrl'].replace("\n", ","))
    else: procData.append('')

    if 'allergy' in list: procData.append(dict['allergy'].replace("\n", ","))
    else: procData.append('')

    if 'imgurl1' in list: procData.append(dict['imgurl1'])
    else: procData.append('')

    if 'manufacture' in list: procData.append(dict['manufacture'].replace("\n", " "))
    else: procData.append('')

    # if 'imagurl2' in list: procData.append(dict['imagurl2'])
    # else: procData.append('')

    return procData


# DB 연결 #
conn = pymysql.connect(host='localhost',user='root',password='2017018023',db='allergydb',charset='utf8')
cur = conn.cursor()

# TABLE 생성 Query문 #
cur.execute("""CREATE TABLE IF NOT EXISTS searchapp_product(
            prdlstReportNo INTEGER NOT NULL,
            prdlstNm varchar(200),
            prdkind varchar(200),
            rawmtrl TEXT,
            allergy TEXT,
            image varchar(100),
            manufacture varchar(200),
            PRIMARY KEY (prdlstReportNo))""")

# json파일 불러오기 #
try:
    serviceKey = "KRFgFYY3tfo9A3cGfNrr%2Bzaib9lhbXTPnsWS149Apg2Vg%2Frl%2BaI9cVAVMQoMPFzLW23jYOdrysnHWISruWgzTA%3D%3D"
    pageNo = 1

    while True:
        URL = "http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService"
        parameters = {"serviceKey" : unquote(serviceKey), "pageNo" : str(pageNo), "returnType" : "json"}
        res = requests.get(URL, params=parameters, verify=False)

        print(res.url)

        if res:
            print(5)
            data = json.loads(res.text)

            body = data['body']
            item_lst = body['items']

            for i in item_lst:
                prdlst = i['item']
                field = prdlst.keys()

                procData = Processed(prdlst, field)

                # 수정 필요 #
                cur.execute("INSERT INTO searchapp_product ('prdlstReportNo','prdlstNm','rawmtrl','allergy','manufacture','prdkind','image') VALUES (?,?,?,?,?,?,?)", procData)
                conn.commit()
            
            pageNo += 1

        else:
            print(6)
            break
finally:
    conn.close()