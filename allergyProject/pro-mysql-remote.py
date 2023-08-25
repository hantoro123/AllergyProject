from urllib.parse import unquote
import requests
import json
import pymysql

# dictionary인 prdlst를 tuple인 procData로 변경 #
def Processed(dict):
    try:
        procData = (dict['prdlstReportNo'],
                    dict['prdlstNm'],
                    dict['prdkind'],
                    dict['rawmtrl'],
                    dict['allergy'],
                    dict['imgurl1'],
                    dict['manufacture'])
    except KeyError:
        return 0

    # 확인용 #
    # print(procData)

    return procData


# DB 연결 #
conn = pymysql.connect(host='localhost',user='root',password='2017018023',db='allergydb',charset='utf8',connect_timeout=10000)
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

# 공공데이터 크롤링 후 searchapp_product table에 입력 #
try:
    serviceKey = "KRFgFYY3tfo9A3cGfNrr%2Bzaib9lhbXTPnsWS149Apg2Vg%2Frl%2BaI9cVAVMQoMPFzLW23jYOdrysnHWISruWgzTA%3D%3D"
    pageNo = 1

    while True:
        print(pageNo)
        URL = "http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService"
        parameters = {"serviceKey" : unquote(serviceKey), "pageNo" : str(pageNo), "returnType" : "json"}
        res = requests.get(URL, params=parameters, verify=False)

        try:
            data = json.loads(res.text)['body']['items']
        except:
            pass

        if data:
            for i in data:
                prdlst = i['item']

                field = prdlst.keys()
                procData = Processed(prdlst)

                if procData:
                    sql = """INSERT INTO searchapp_product(prdlstReportNo, prdlstNm, prdkind, rawmtrl, allergy, image, manufacture) VALUES(%s, %s, %s, %s, %s, %s, %s)"""\
                        """ON DUPLICATE KEY UPDATE prdlstNm=VALUES(prdlstNm), prdkind=VALUES(prdkind), rawmtrl=VALUES(rawmtrl), allergy=VALUES(allergy), image=VALUES(image), manufacture=VALUES(manufacture)"""

                    cur.execute(sql, procData)
                    conn.commit()
            
            pageNo += 1
        
        else:
            break

finally:
    conn.close()