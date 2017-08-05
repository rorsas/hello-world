django   http://www.runoob.com/django/django-model.html
Bootstrap http://www.bootcss.com/



/usr/local/bin/python3.6  manage.py runserver 0.0.0.0:8002

http://127.0.0.1:8002/hello

/usr/local/bin/python3.6 manage.py migrate


$ python manage.py migrate   # 创建表结构

$ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate TestModel   # 创建表结构
