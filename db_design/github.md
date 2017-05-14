#### github_project
| field      |     type |    comment |
| :-------- | --------:| --------:|
| project_id    |   bigint(11) PRIMARY KEY NOT NULL |   主键  |
| name    |   VARCHAR(100) |    项目名 |
| language    |   VARCHAR(30) |    语言 |
| meta    |   VARCHAR(100) |    star数  |
| des    |   VARCHAR(200) |   项目描述  |
| href    |   VARCHAR(100) |    项目路径  |
| link    |   VARCHAR(100) |    项目链接  |
| owner    |   VARCHAR(100) |    作者或组织  |

#### github_project_contributors
| field      |     type |    comment |
| :-------- | --------:| --------:|
| contributors_id    |   bigint(11) PRIMARY KEY NOT NULL | 主键|
| project_id    |   bigint(11) NOT NULL |  项目id|
| name    |   varchar(100) | 贡献者name|
| avatar    |   varchar(100) | 贡献者头像|