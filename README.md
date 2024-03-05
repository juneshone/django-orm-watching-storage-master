# Пульт охраны банка

Веб-сайт для отслеживания посетителей хранилища. В проекте используется база данных, в которой фиксируются все посещения.Без доступа к базе данных вы не сможете запустить проект, но можете посмотреть как реализованы запросы к базе данных.

## Как установить

Склонируйте репозиторий. Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```

Создайте файл .env, в котором будут храниться чувствительные данные. Для подключения к базе данных задайте переменные окружения: 

* `DATABASES_URL` переменная, которая выглядит так `postgresql://username:password@host:port/name`.
* `SECRET_KEY` секретный ключ сайта.
* `DEBUG_VALUE` значение, которое включает / выключает режим отладки. По умолчанию `False`.
* `ALLOWED_HOSTS` список хостов/доменов, для которых может работать текущий сайт.

Для запуска проекта и вывода данных на сайте выполните команду:

```python
python manage.py runserver
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.