# YaCut

## Описание
Yacut - cервис укорачивания ссылок, который заменяет длинную ссылку на короткую (до 16 символов).
Вариант сокращения может быть задан как самим пользователем, так и сгенерирован автоматически сервисом.
Все сокращения уникальны. Реализован Web-интерфейс для пользователей и REST API.

### Основные эндпоинты
/ - Web-интерфейс для генерации короткой ссылки

/<short_id>/ - Web-интерфейс для переадресации на исходную ссылку

/api/id/ - POST-запрос к API для генерации короткой ссылки

/api/id/<short_id>/ - GET-запрос для получения исходной ссылки из короткой


## Применяемые технологии

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)

### Порядок действий для запуска проекта

Клонировать репозиторий и перейти в папку c проектом:

```
git clone git@github.com:ItsFreez/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

*Для Windows*
```
python -m venv env
source venv/Scripts/Activate
```
*Для MacOS/Linux*
```
python3 -m venv env
source env/bin/activate
```

Обновить менеджер pip и установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Применить миграции для создания базы данных

```
flask db upgrade
```

Запуск сервера (перед этим не забудьте выставить нужные настройки в файле .env)
```
flask run
```

### Автор проекта

[ItsFreez](https://github.com/ItsFreez)
