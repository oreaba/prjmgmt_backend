cp .env.local .env
source /D/prjmgmt_backend/.venv/Scripts/activate
python manage.py makemigrations
python manage.py migrate
python manage.py mysuperuser
python manage.py collectstatic
python manage.py runserver 127.0.0.1:8000