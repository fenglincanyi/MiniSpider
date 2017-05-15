import time

def datestr_to_timestamp(t):
    t = t[0: t.index('.')].replace('T', ' ')
    timeArray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    return long(time.mktime(timeArray))


# datestr_to_timestamp("2017-05-10T04:23:58.067Z")