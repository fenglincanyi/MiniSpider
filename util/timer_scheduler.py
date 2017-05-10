# coding=utf-8
from apscheduler.schedulers.blocking import BlockingScheduler

import db_handle

sched = BlockingScheduler()


def timer(jobName, sec):
    sched.add_job(jobName, 'interval', seconds=sec)
    sched.start()


def timer_stop():
    print "===任务停止==="
    sched.shutdown()
    db_handle.close() # 数据库断开连接
