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
# conn.select_db('pymysql_demo')
# conn.select_db('maimai_demo')
conn.select_db('toutiao_demo')


def create_table():
    try:
        # # 创建表
        # TABLE_NAME = 'github_project'
        # cursor.execute('CREATE TABLE %s('
        #                'project_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL ,'
        #                'name VARCHAR(100) NOT NULL ,'
        #                'language VARCHAR(30) NOT NULL ,'
        #                'meta VARCHAR(100) NOT NULL ,'
        #                'des VARCHAR(255) NOT NULL, '
        #                'href VARCHAR(100) NOT NULL ,'
        #                'link VARCHAR(100) NOT NULL ,'
        #                'owner VARCHAR(100) NOT NULL)' % TABLE_NAME)
        #
        # TABLE_NAME = 'github_project_contributors'
        # cursor.execute('CREATE TABLE %s('
        #                'contributors_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL ,'
        #                'project_id BIGINT(11) NOT NULL ,'
        #                'name VARCHAR(100) NOT NULL ,'
        #                'avatar VARCHAR(100) NOT NULL)' % TABLE_NAME)

        # -----------------------------------------------------------------------------------------------------

        # TABLE_NAME = 'maimai_list'
        # cursor.execute('CREATE TABLE %s('
        #                'list_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,'
        #                'text VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,'
        #                'note NVARCHAR(50) NOT NULL,'
        #                'likes INT NOT NULL,'
        #                'cmts INT NOT NULL, '
        #                'time NVARCHAR(50) NOT NULL) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci' % TABLE_NAME)
        #
        # TABLE_NAME = 'maimai_pics'
        # cursor.execute('CREATE TABLE %s('
        #                'pics_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,'
        #                'list_id BIGINT(11) NOT NULL,'
        #                'turl VARCHAR(255) NOT NULL,'
        #                'url VARCHAR(255) NOT NULL)' % TABLE_NAME)
        #
        # TABLE_NAME = 'maimai_tags'
        # cursor.execute('CREATE TABLE %s('
        #                'tag_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,'
        #                'list_id BIGINT(11) NOT NULL,'
        #                'tag NVARCHAR(100) NOT NULL)' % TABLE_NAME)
        #
        # TABLE_NAME = 'maimai_comments'
        # cursor.execute('CREATE TABLE %s('
        #                'comments_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,'
        #                'list_id BIGINT(11) NOT NULL,'
        #                'name VARCHAR(100) NOT NULL,'
        #                'text VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,'
        #                'prefix NVARCHAR(30) NOT NULL,'
        #                'avatar VARCHAR(255) NOT NULL,'
        #                'likes INT NOT NULL)' % TABLE_NAME)


        # -----------------------------------------------------------------------------------------------------

        TABLE_NAME = 'toutiao_media_info'
        cursor.execute('CREATE TABLE %s('
                       'media_info_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,'
                       'avatar_url VARCHAR(255) NOT NULL,'
                       'name NVARCHAR(100) NOT NULL)' % TABLE_NAME)

        TABLE_NAME = 'toutiao_list'
        cursor.execute('CREATE TABLE %s('
                       'list_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,'
                       'media_info_id BIGINT(11) NOT NULL,'
                       'title NVARCHAR (100) NOT NULL,'
                       'abstract NVARCHAR(255) NOT NULL,'
                       'publish_time long NOT NULL,'
                       'read_count INT NOT NULL,'
                       'comment_count INT NOT NULL,'
                       'share_count INT NOT NULL,'
                       'article_url VARCHAR(255) NOT NULL,'
                       'share_url VARCHAR(255) NOT NULL)' % TABLE_NAME)

        TABLE_NAME = 'toutiao_list_image'
        cursor.execute('CREATE TABLE %s('
                       'list_image_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,'
                       'list_id BIGINT(11) NOT NULL,'
                       'url VARCHAR(255) NOT NULL)' % TABLE_NAME)

        TABLE_NAME = 'toutiao_list_keywords'
        cursor.execute('CREATE TABLE %s('
                       'list_keywords_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,'
                       'list_id BIGINT(11) NOT NULL,'
                       'keyword VARCHAR(30) NOT NULL)' % TABLE_NAME)

        TABLE_NAME = 'toutiao_list_filter_words'
        cursor.execute('CREATE TABLE %s('
                       'list_keywords_id BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,'
                       'list_id BIGINT(11) NOT NULL,'
                       'name NVARCHAR(50) NOT NULL)' % TABLE_NAME)


    except:
        import traceback

        traceback.print_exc()
        conn.rollback()

    finally:
        cursor.close()
        conn.close()


def insert(data):
    # sql1 = "INSERT INTO github_project(name, language, meta, des, href, link, owner) values('%s', '%s','%s', '%s','%s', '%s','%s')"
    # sql2 = "INSERT INTO github_project_contributors(project_id, name, avatar) values('%s', '%s','%s')"
    # try:
    #     for e in data:
    #         cursor.execute(sql1 % (e['project']['name'], e['project']['language'],
    #                                e['project']['meta'], github_transform.remove_emoji(e['project']['des']),
    #                                e['project']['href'], e['project']['link'],
    #                                e['project']['owner']))
    #
    #         project_id = int(conn.insert_id())
    #         for c in e['contributors']:
    #             cursor.execute(sql2 % (project_id, c['name'], c['avatar']))



    # -----------------------------------------------------------------------------------------------------


    # sql1 = "INSERT INTO maimai_list(text, note, likes, cmts, time) values('%s','%s', '%s','%s', '%s')"
    # sql2 = "INSERT INTO maimai_pics(list_id, turl, url) values('%s', '%s', '%s')"
    # sql3 = "INSERT INTO maimai_tags(list_id, tag) values('%s','%s')"
    # sql4 = "INSERT INTO maimai_comments(list_id, name, text, prefix, avatar, likes) values('%s','%s','%s', '%s','%s', '%s')"
    # try:
    #     for e in data:
    #         cursor.execute(sql1 % (e['text'], e['note'], e['likes'], e['cmts'], e['time']))
    #
    #         list_id = int(conn.insert_id())
    #
    #         for c in e['pics']:
    #             cursor.execute(sql2 % (list_id, c['turl'], c['url']))
    #
    #         if e['tags']:
    #             tags = e['tags'].split(',')
    #             for i in tags:
    #                 cursor.execute(sql3 % (list_id, i))
    #
    #         for c in e['comments']:
    #             cursor.execute(sql4 % (list_id, c['name'], c['text'], c['prefix'], c['avatar'], c['likes']))


    # -----------------------------------------------------------------------------------------------------

    sql1 = "INSERT INTO toutiao_media_info(avatar_url, name) values('%s','%s')"
    sql2 = "INSERT INTO toutiao_list(media_info_id, title, abstract, publish_time, read_count, comment_count, share_count, article_url, share_url) values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
    sql3 = "INSERT INTO toutiao_list_image(list_id, url) values('%s','%s')"
    sql4 = "INSERT INTO toutiao_list_keywords(list_id, keyword) values('%s','%s')"
    sql5 = "INSERT INTO toutiao_list_filter_words(list_id, name) values('%s','%s')"

    try:
        for e in data:
            content = json.loads(e['content']) # 头条的接口定义不规范，content 对应 的值是一个  "" 包裹的 json 对象

            media_info_id = -1 # 代表没有 媒体
            if content.has_key('media_info'):
                cursor.execute(sql1 % (content['media_info']['avatar_url'], content['media_info']['name']))
                media_info_id = int(conn.insert_id())



            if not content['abstract']:
                abstract = ''
            else:
                abstract = content['abstract']

            if not content['share_count']:
                share_count = 0
            else:
                share_count = content['share_count']

            cursor.execute(sql2 % (media_info_id, content['title'], abstract, content['publish_time'], content['read_count'], content['comment_count'], share_count, content['article_url'], content['share_url']))


            list_id = int(conn.insert_id())

            if content['image_list']:
                for i in content['image_list']:
                    cursor.execute(sql3 % (list_id, i['url']))

            if content.has_key('keywords') and content['keywords']:
                tmp = content['keywords'].split(',')
                for i in tmp:
                    cursor.execute(sql4 % (list_id, i))

            if content['filter_words']:
                for i in content['filter_words']:
                    cursor.execute(sql5 % (list_id, i['name']))

    except:
        import traceback

        traceback.print_exc()
        conn.rollback()

    finally:
        cursor.close()
        conn.close()
