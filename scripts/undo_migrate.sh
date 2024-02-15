# undo migration of django tables:
python manage.py migrate auth zero    
python manage.py migrate admin zero              
python manage.py migrate contenttypes zero
python manage.py migrate sessions zero

python manage.py migrate users zero
python manage.py migrate projects zero
python manage.py migrate organizations zero


rm organizations/migrations/*.*
rm projects/migrations/*.*
rm tasks/migrations/*.*
rm users/migrations/*.*

# delete migration table manually
# DROP TABLE DJANGO_MIGRATIONS CASCADE CONSTRAINTS;