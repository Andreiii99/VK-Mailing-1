#Предзапуск:
    
    1.Установить requirements.txt пакеты.
    2.Установить домен в apps/main/migrations/0001_initial.py (по-умолчанию localhost:8000)
    3.Задать параметры БД в settings.py проекта.
    3.Выполнить команды `python manage.py migrate main && python manage.py migrate`
