# Generated by Django 5.0 on 2024-03-11 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='program',
        ),
    ]
