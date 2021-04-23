Як запустити програму?
---------------------------------------
1. Відкрийте в терміналі свою основну папку проекту. Створіть та активуйте віртуальне середовище.
* cd main_project_folder
* virtualenv venv
* Scripts\activate.bat
2. Встановіть залежності та ці пакети.
* pip install django gunicorn whitenoise dj-database-url psycopg2
3.ініціалізуйте репозиторій.
* git init
* git add .
* git commit -am "init message" 
4. Залогіньте свій акаунт heroku
* heroku login
5. Створіть heroku арр
*heroku create
6. Створіть базу даних для додатку
*heroku addons:create heroku-postgresql:hobby-dev
*heroku config -s
7. Вимкніть Collectstatic і перенесіть файли на heroku.
*heroku config:set DISABLE_COLLECTSTATIC=1
*git push heroku main
8. Запускаєте файл
*python manage.py migrate
9. Відкриваєте консоль
*heroku run bush
10. Робите міграцію у базу
*manage.py migrate
11. Створюєте користувача
*manage.py createsuperuser
(логін, пароль бажано admin, 123pass123,бо в підказці html саме ці логін та пароль)
12. Заповнєте базу виконавцями
*manage.py import_from_csv aug_train.csv
13. Відкриваєте сайт 
*heroku open


Приклад сайту, що розгорнула я
https://pacific-shore-49299.herokuapp.com/
Схема бази даних в файлі diagram.png
Сайт надає можливість користувачам проглядати людей, які можуть виконати роботу.
Адмін має право видаляти та додавати робітників.
