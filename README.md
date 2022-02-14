### О проекте:
Проект Yatube_API реализован на базе моделей Django. Его функционал включает работу с проектом через API.


### Как запустить проект на виртуальном сервере:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/jletova/api_final_yatube
```

Перейти в папку проекта:

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```


### Примеры:

Подробная документация по API с примерами расположена по ссылке:

```
(http://127.0.0.1:8000/redoc/)
```