# BlogA【这是一个完全依赖cursor完成的项目】

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

## 安装步骤

1. 克隆项目到本地：

   ```bash
   git clone https://github.com/yourusername/blogA.git
   cd blogA
   ```

2. 创建虚拟环境并激活：

   ```bash
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
   ```

3. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

4. 配置数据库：

   在 `config.py` 文件中配置你的 MySQL 数据库连接：

   ```python
   class Config:
       SECRET_KEY = 'your-secret-key'
       SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/flask_blog'
       SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

5. 初始化数据库：

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. 运行应用：

   ```bash
   flask run
   ```

7. 在浏览器中访问 `http://localhost:5000`。

## 使用说明

- 注册新用户并登录。
- 登录后可以发布、编辑和删除博文。
- 管理员可以管理用户和博文。

## 贡献

欢迎提交问题和贡献代码。请 fork 本项目并提交 pull request。

## 许可证

本项目使用 MIT 许可证。详细信息请参阅 LICENSE 文件。

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)