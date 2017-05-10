# coding=utf-8
import pymongo

connection = pymongo.MongoClient('localhost', 27017)
# coll_test_list = connection.test.test_list  # test_list collection（表）
# coll_test_geng = connection.test.test_geng  # test_geng collection（表）


# 插入数据库
def list_insert(db_name, collection_name, data):
    coll = connection[db_name][collection_name]

    # print data
    # print type(coll_test_geng)

    # pymongo.collection.Collection 中：  insert()过时了
    # warnings.warn("insert is deprecated. Use insert_one or insert_many "instead.", DeprecationWarning, stacklevel=2)



    # 批量插入, 插入的对象 必须是 字典实例、python 对象
    coll.insert_many(data)
    # coll.insert_one(data)


def close():
    connection.close()


    # list_insert('test','aaa', {"aaa":"aaaa"})
