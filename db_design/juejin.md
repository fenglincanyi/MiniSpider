#### juejin_user

| field      |     type |   comment   |
| :-------- | --------:| :------: |
| user_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| username    | NVARCHAR(50) NOT NULL |  用户名 |
| email    | VARCHAR(100) NOT NULL |  邮箱|
| github_html_url    | VARCHAR(255) NOT NULL |  github 链接|
| wechat_nickname    | NVARCHAR(50) NOT NULL |  微信昵称|
| company    | NVARCHAR(100) NOT NULL |  所在公司|
| jobTitle    | NVARCHAR(100) NOT NULL | 职位名称|
| blogAddress    | VARCHAR(255) NOT NULL | blog 地址|
| self_description    | NVARCHAR(255) NOT NULL | 自我介绍|

#### juejin_list_tag
| field      |     type |   comment   |
| :-------- | --------:| :------: |
| list_tag_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| name    |   NVARCHAR(50) NOT NULL |  标签名  |

#### juejin_list
| field      |     type |   comment   |
| :-------- | --------:| :------: |
| list_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| user_id    |   BIGINT(11) NOT NULL |  用户id |
| tag_ids    |   VARCHAR(50) NOT NULL |  标签id |
| title    |   NVARCHAR(100) NOT NULL |  标题 |
| content    |   NVARCHAR(255) NOT NULL |  内容 |
| collectionCount    |  int NOT NULL |  收藏数 |
| commentsCount    |  int NOT NULL |  评论数 |
| url    |  VARCHAR(255) NOT NULL |  文章链接  |
| createdAt    | long NOT NULL |  创建时间 |