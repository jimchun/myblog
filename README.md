# blogA
all coding by CURSOR
�봴��һ��blog���򣬾������£�

����ջ��
- ���: Flask (Python web���)
- ���ݿ�: MySQL���������ݿ�root���룺Zoe@9820
- ǰ��: HTML/CSS/JavaScript (����ʹ��Bootstrap�ȿ��)

ʵ�ֹ��ܣ�
4. �û�ע�Ṧ��
- ����ע�����
- ��֤�������ݡ�
- ���û����ݴ洢�����ݿ⡣

5. �û����Ĺ���
- �������ķ�������
- ʵ�ֲ��ĵ�CRUD����������ȡ�����¡�ɾ����������

6. ����Ա����
- ʵ�ֹ���Ա��¼��
- �ṩ�����û��Ͳ��ĵĽ��档

7. �ṩ�������ݵĳ�ʼ������

�õ�,����Ϊ������һ������Flask�Ĳ��ͳ������ǽ��ֲ���ʵ�������Ŀ������,������������Ŀ�ṹ�ͻ������á�


1. ��Ŀ�ṹ:

```
blog/
��
������ app/
��   ������ __init__.py
��   ������ models.py
��   ������ routes.py
��   ������ templates/
��       ������ base.html
��       ������ index.html
��       ������ register.html
��       ������ login.html
��       ������ post.html
��       ������ admin/
��           ������ dashboard.html
��           ������ users.html
��           ������ posts.html
��
������ config.py
������ run.py
������ requirements.txt
```

2. ��װ��Ҫ�İ�:
���� `requirements.txt` �ļ�:
Flask==2.1.0
Flask-SQLAlchemy==2.5.1
Flask-Login==0.5.0
Flask-WTF==0.15.1
mysqlclient==2.0.3

Ȼ������:
pip install -r requirements.txt
