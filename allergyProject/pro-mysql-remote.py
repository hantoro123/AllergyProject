from urllib.parse import unquote
import requests
import json
import pymysql

# dictionary인 prdlst를 tuple인 procData로 변경 #
def Processed(dict):

    procData = (dict['prdlstReportNo'],
                dict['prdlstNm'],
                dict['prdkind'],
                dict['rawmtrl'],
                dict['allergy'],
                dict['imgurl1'],
                dict['manufacture'])

    # 확인용 #
    # print(procData)

    return procData


# DB 연결 #
conn = pymysql.connect(host='localhost',user='root',password='2017018023',db='allergydb',charset='utf8')
cur = conn.cursor()

# TABLE 생성 Query문 #
cur.execute("""CREATE TABLE IF NOT EXISTS searchapp_product(
            prdlstReportNo varchar(200) NOT NULL,
            prdlstNm varchar(200),
            prdkind varchar(200),
            rawmtrl TEXT,
            allergy TEXT,
            image varchar(100),
            manufacture varchar(200),
            PRIMARY KEY (prdlstReportNo))""")

# TABLE DATA 초기화 (테스트용) #
cur.execute("""DELETE FROM searchapp_product""")

# 공공데이터 크롤링 후 searchapp_product table에 입력 #
try:
    serviceKey = "KRFgFYY3tfo9A3cGfNrr%2Bzaib9lhbXTPnsWS149Apg2Vg%2Frl%2BaI9cVAVMQoMPFzLW23jYOdrysnHWISruWgzTA%3D%3D"
    pageNo = 1

    while True:
        URL = "http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService"
        parameters = {"serviceKey" : unquote(serviceKey), "pageNo" : str(pageNo), "returnType" : "json"}
        res = requests.get(URL, params=parameters, verify=False)

        if res:
            data = json.loads(res.text)['body']['items']

            for i in data:
                prdlst = i['item']

                field = prdlst.keys()
                procData = Processed(prdlst)

                # 수정 필요 #
                # 사항 : data가 없으면 insert 있으면 update #
                cur.execute("""INSERT INTO searchapp_product(prdlstReportNo, prdlstNm, prdkind, rawmtrl, allergy, image, manufacture) VALUES(%s, %s, %s, %s, %s, %s, %s)""", procData)
                conn.commit()
            
            pageNo += 1

        else:
            break

finally:
    conn.close()