# prjmgmt_backend
# one liner ssh connect
    ssh -i "~/.ssh/adm-prjmgmt-aws-eb-key" ec2-user@ec2-157-175-207-193.me-south-1.compute.amazonaws.com

    cd /efs-adm-pm-db-prod/
    ls -lrt
    sudo chmod 664 /efs-adm-pm-db-prod/


    source /var/app/venv/staging-$$$$$/bin/activat

    cd /var/app/current/
    python manage.py createsuperuser


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

