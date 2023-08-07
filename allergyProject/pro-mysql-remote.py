import pymysql

conn = pymysql.connect(host='localhost',user='root',password='2017018023',charset='utf8')
cursor = conn.cursor()

# 쿼리문 작성 #

conn.commit()
conn.close()