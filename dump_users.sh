python manage.py dumpdata users.PMUser --indent 2 > users_pmuser.json
python manage.py dumpdata auth.Group --indent 2 > groups.json
python manage.py dumpdata admin.LogEntry --indent 2 > adminlogentry.json
python manage.py dumpdata projects.projecttype --indent 2 > projecttype.json