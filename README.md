## Тестовое задание от Сириуса
### Описание
---
Данный проект представляет собой Django проект позоляющий сохранять картники и описание к ним 

### Используемые технологии
---
* Python 3.11.6;
* Django
* Django REST Framework
* MySQL(Реляционая база данных)
* Requests

### О проекте
---

<details>
<summary>ТЗ проекта ↓</summary>
Реализовать API с 3мя эндпоинтами.
1.1. Принимает json с картинкой (base64) и описание картинки в виде текста.
1.2. Отдает список картинок с описанием.
1.3. Удаляет картинку из бд по ID.

Реализовать интерфейс который общается с API из пункта 1.
2.1. Форма по отправке картинки с описанием.
2.2. Список всех картинок с кнопкой удаления.
</details>


### Запуск проекта
---
1. Клонируем:
``` git clone https://github.com/Sodx1/TestSirus.git/```
2. Устанавливаем venv и активируем его:
```
cd sirus
python -m venv venv
cd venv/Scripts
activate.bat
```
4. Устанавливаем зависимости из requirements.txt
``` pip install -r requirements.txt ```
5. Устанавливаем зависимости из requirements.txt
```Делаем все миграции для этого используйте MySQL. Все параметры находится в файле setings.py```
6. Запускаем приложение:
```
python manage.py runserver
```

### Используемые API
---
- Погода - http://api.openweathermap.org
- Конвертер валют - https://api.apilayer.com
- Животные - https://random.dog и https://randomfox.ca
