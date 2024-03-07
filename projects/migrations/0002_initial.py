# Generated by Django 5.0 on 2024-03-07 09:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managed_project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.program'),
        ),
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.projectpriority'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.projectstatus'),
        ),
        migrations.AddField(
            model_name='projectuser',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project'),
        ),
        migrations.AddField(
            model_name='projectuser',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.role'),
        ),
        migrations.AddField(
            model_name='projectuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='projectuser',
            unique_together={('project', 'user', 'role')},
        ),
    ]
