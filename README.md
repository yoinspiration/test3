# 使用说明

1. 在命令行中依次输入以下命令

```shell
pip install Django
pip install django-cors-headers
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

如果提示找不到`python`的话，可以尝试把`python`改成`python3`, 也有可能是您的电脑上还没安装`Python`, 或者是还没把`python`添加到`path`环境变量里

2.  然后在浏览器中输入网址`http://127.0.0.1:8000/`, `8000`表示端口号，如果被占用的话，可能会自动改成别的端口号，比如`8001`，请留意命令行界面的提示，比如`Starting development server at http://127.0.0.1:8000/`
