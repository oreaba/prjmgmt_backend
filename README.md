# prjmgmt_backend
# one liner ssh connect
    ssh -i "~/.ssh/adm-prjmgmt-aws-eb-key" ec2-user@ec2-157-175-186-225.me-south-1.compute.amazonaws.com

# one liner to create super user:
sudo source /var/app/current/superuser.sh

    "echo 'from django.contrib.auth.models import User; User.objects.create_superuser(\"admin\", \"admin\", \"m.h.oreaba@gmail.com\")' | python manage.py shell"  
    
# one liner deploy
git add . && git commit -m "dev" && git push && eb deploy

option_settings:
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: production.settings
  aws:elasticbeanstalk:environment:proxy:
    ProxyServer: apache
  aws:elasticbeanstalk:environment:proxy:staticfiles:
    /html: statichtml
    /images: staticimages
  aws:elasticbeanstalk:container:python:
    WSGIPath: ebdjango.wsgi:application
    NumProcesses: 3
    NumThreads: 20


option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: prjmgmt.wsgi:application


aws:elasticbeanstalk:environment:proxy:staticfiles:
    /static: static



## angular frontend
"start": "ng serve --baseHref=",
"build": "ng build --baseHref=/static/website/",
