sudo chmod 777 /efs-adm-pm-db-prod/adm-pm.db.sqlite3
source /var/app/venv/staging-*/bin/activate
cd /var/app/current/
python manage.py createsuperuser