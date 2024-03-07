cp .env.local .env
source /D/prjmgmt_backend/.venv/Scripts/activate
python manage.py makemigrations < <(yes y)
python manage.py migrate
python manage.py loaddata data/users_pmuser.json
# python manage.py mysuperuser
python manage.py collectstatic < <(yes yes)
python manage.py runserver 127.0.0.1:8000
