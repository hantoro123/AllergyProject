import pymysql

conn = pymysql.connect(host='localhost',user='root',password='2017018023',db='allergydb',charset='utf8')
cursor = conn.cursor()

sql = """CREATE TABLE test(
    id INT,
    PRIMARY KEY(id)
);
"""

cursor.execute(sql)
cursor.execute("SHOW TABLES")

conn.commit()
conn.close()