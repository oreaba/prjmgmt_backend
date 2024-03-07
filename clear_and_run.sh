rm local_db/*.*

rm users/migrations/0*.*
rm projects/migrations/0*.*
rm tasks/migrations/0*.*
rm organizations/migrations/0*.*

# you must have this file for makemigrations to work: touch appname/migrations/__init__.py
source run.sh