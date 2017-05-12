# coding=utf-8
import pymysql
import json
from transform import github_transform

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'charset': 'utf8',
}

conn = pymysql.connect(**config)
conn.autocommit(True)  # 设置自动提交，否则，执行插入 更新操作不生效

cursor = conn.cursor()
# 连接数据库
conn.select_db('pymysql_demo')


def create_table():
    try:
        # 创建表
        TABLE_NAME = 'github_project'
        cursor.execute('CREATE TABLE %s('
                       'project_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL ,'
                       'name VARCHAR(100) NOT NULL ,'
                       'language VARCHAR(30) NOT NULL ,'
                       'meta VARCHAR(100) NOT NULL ,'
                       'des VARCHAR(255) NOT NULL, '
                       'href VARCHAR(100) NOT NULL ,'
                       'link VARCHAR(100) NOT NULL ,'
                       'owner VARCHAR(100) NOT NULL)' % TABLE_NAME)

        TABLE_NAME = 'github_project_contributors'
        cursor.execute('CREATE TABLE %s('
                       'contributors_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL ,'
                       'project_id BIGINT(11) NOT NULL ,'
                       'name VARCHAR(100) NOT NULL ,'
                       'avatar VARCHAR(100) NOT NULL)' % TABLE_NAME)

    except:
        import traceback

        traceback.print_exc()
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def insert(data):
    sql1 = "INSERT INTO github_project(name, language, meta, des, href, link, owner) values('%s', '%s','%s', '%s','%s', '%s','%s')"
    sql2 = "INSERT INTO github_project_contributors(project_id, name, avatar) values('%s', '%s','%s')"
    try:
        for e in data:
            cursor.execute(sql1 % (e['project']['name'], e['project']['language'],
                                   e['project']['meta'], github_transform.remove_emoji(e['project']['des']),
                                   e['project']['href'], e['project']['link'],
                                   e['project']['owner']))

            project_id = int(conn.insert_id())
            for c in e['contributors']:
                cursor.execute(sql2 % (project_id, c['name'], c['avatar']))

    except:
        import traceback

        traceback.print_exc()
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
