# coding=utf-8
import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'charset': 'utf8',
}

conn = pymysql.connect(**config)
conn.autocommit(True) # 设置自动提交，否则，执行插入 更新操作不生效

cursor = conn.cursor()

try:
    # 连接数据库
    conn.select_db('pymysql_demo')

    # # 创建表
    # TABLE_NAME = 'users'
    # cursor.execute('CREATE TABLE %s('
    #                'project_id char(10) PRIMARY KEY NOT NULL ,'
    #                'name VARCHAR(50),'
    #                'language VARCHAR(30),'
    #                'meta VARCHAR(30),'
    #                'des VARCHAR(200),'
    #                'href VARCHAR(100),'
    #                'link VARCHAR(100),'
    #                'contributors_id VARCHAR(10),'
    #                'owner VARCHAR(30))' % TABLE_NAME)




  # 创建表
  #   TABLE_NAME = 'user'
  #   cursor.execute('CREATE TABLE %s(id int primary key,name varchar(30))' %TABLE_NAME)

    # 批量插入纪录
    values = []
    for i in range(20):
        values.append((i, 'kk' + str(i)))
    cursor.executemany('INSERT INTO user values(%s,%s)', values)

except:
    import traceback

    traceback.print_exc()
    conn.rollback()

finally:
    cursor.close()
    conn.close()
