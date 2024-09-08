# BlogA

这是一个基于 Flask 的博客项目。

## 项目简介

BlogA 是一个简单的博客系统，用户可以注册、登录、发布博文、编辑博文和删除博文。管理员可以管理用户和博文。

## 技术栈

- 后端: Flask (Python Web 框架)
- 数据库: MySQL
- 前端: HTML/CSS/JavaScript (使用 Bootstrap)

## 功能

1. 用户注册和登录
2. 用户发布博文
3. 用户编辑和删除自己的博文
4. 管理员管理用户和博文

## 项目结构

```
blog/

 app/
   __init__.py
   models.py
   routes.py
   templates/
       base.html
       index.html
       register.html
       login.html
       post.html
       admin/
           dashboard.html
           users.html
           posts.html

 config.py
 run.py
 requirements.txt
```

2. װҪİ:
 `requirements.txt` ļ:
Flask==2.1.0
Flask-SQLAlchemy==2.5.1
Flask-Login==0.5.0
Flask-WTF==0.15.1
mysqlclient==2.0.3

Ȼ:
pip install -r requirements.txt
