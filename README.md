# prjmgmt_backend
    ssh -i "~/.ssh/adm-prjmgmt-aws-eb-key" ec2-user@ec2-157-175-205-15.me-south-1.compute.amazonaws.com


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

