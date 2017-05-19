#### maimai_list

| field      |     type |   comment   |
| :-------- | --------:| :------: |
| list_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| text    | VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL(带表情) |  文本内容  |
| note    |   NVARCHAR(50) NOT NULL |  标签  |
| likes    |   int NOT NULL |  喜欢数  |
| cmts    |   int NOT NULL |  评论数  |
| time    |   NVARCHAR(50) NOT NULL |  时间  |
#### maimai_pics
| field      |     type |   comment   |
| :-------- | --------:| :------: |
| pics_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| list_id    | BIGINT(11) NOT NULL |  list id|
| turl    | VARCHAR(255) NOT NULL |  缩略图  |
| url    | VARCHAR(255) NOT NULL |  原图  |
#### maimai_tags
| field      |     type |   comment   |
| :-------- | --------:| :------: |
| tag_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| list_id    | BIGINT(11) NOT NULL |  list id|
| tag    | NVARCHAR(100) NOT NULL |  标签名|

#### maimai_comments
| field      |     type |   comment   |
| :-------- | --------:| :------: |
| comments_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| list_id    |   BIGINT(11) NOT NULL |  list id  |
| name  |  VARCHAR(100) NOT NULL |  评论人name |
| text  | VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL(带表情的) |  评论内容 |
| prefix  |  NVARCHAR(30) NOT NULL |  评论开头 |
| avatar  |  VARCHAR(255) NOT NULL |  评论人头像|
| likes  |  int NOT NULL |  喜欢数|