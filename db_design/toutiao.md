#### toutiao_media_info
| field      |     type |   comment   |
| :-------- | --------:| :------: |
| media_info_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| avatar_url    |   VARCHAR(255) NOT NULL |  头像  |
| name    |   NVARCHAR(100) NOT NULL |  name  |

#### toutiao_list_filter_words
| field      |     type |   comment   |
| :-------- | --------:| :------: |
| list_filter_words_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| name    |   NVARCHAR(100) NOT NULL |  name  |


#### toutiao_list
| field      |     type |   comment   |
| :-------- | --------:| :------: |
| list_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| media_info_id    |   BIGINT(11) NOT NULL |  头像  |
| list_filter_words_ids    |   VARCHAR(100) NOT NULL |  过滤词ids  |
| title    |   NVARCHAR(100) NOT NULL | 标题  |
| abstract    |   NVARCHAR(255) NOT NULL | 文章摘要  |
| publish_time    |   long NOT NULL | 发布时间 |
| read_count    |   int NOT NULL | 阅读量|
| comment_count    |   int NOT NULL | 评论量 |
| share_count    |   int NOT NULL | 分享量|
| article_url    |   VARCHAR(255) NOT NULL | 文章url|
| share_url    |   VARCHAR(255) NOT NULL | 分享url|

#### toutiao_list_image
| field      |     type |   comment   |
| :-------- | --------:| :------: |
| list_image_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| list_id    |   BIGINT(11) NOT NULL |  list id  |
| url    |   VARCHAR(255) NOT NULL |  图片url |

#### toutiao_list_keywords
| field      |     type |   comment   |
| :-------- | --------:| :------: |
| list_keywords_id    |   BIGINT(11) PRIMARY KEY AUTO_INCREMENT NOT NULL |  主键  |
| list_id    |   BIGINT(11) NOT NULL |  list id  |
| keyword    |   VARCHAR(30) NOT NULL |  关键词 |




