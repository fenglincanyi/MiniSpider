用户信息表

id
username
phone
email 
pwd 加盐后
salt varchar
recent_pwd varchar()
user_status int
crt_ts timestamp


redis :
 Set 存锁定用户，一小时重试