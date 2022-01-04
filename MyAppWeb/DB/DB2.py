import pymysql

##数据库相关信息
host = "49.235.64.91"
port = 3306
user = "sht"
password = "shtsht"
db_name = "sht"


def insert(sql, args):
    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db_name)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()


def query_all(sql, args):
    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db_name)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    all_query = cursor.fetchall()
    cursor.close()
    conn.close()
    return all_query


def query_one(sql, args):
    conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db_name)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    one_query = cursor.fetchone()
    cursor.close()
    conn.close()
    return one_query
