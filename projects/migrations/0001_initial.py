# Generated by Django 5.0.2 on 2024-02-15 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('portfolio_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ar', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolio',
            },
        ),
        migrations.CreateModel(
            name='ProjectPriority',
            fields=[
                ('priority_id', models.AutoField(primary_key=True, serialize=False)),
                ('priority', models.CharField(max_length=50)),
                ('priority_ar', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(max_length=7)),
            ],
            options={
                'verbose_name': 'Project Priority',
                'verbose_name_plural': 'Project Priority',
            },
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
                ('status_ar', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(max_length=7)),
            ],
            options={
                'verbose_name': 'Project Status',
                'verbose_name_plural': 'Project Status',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('name_ar', models.CharField(blank=True, max_length=100, null=True)),
                ('portfolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.portfolio')),
            ],
            options={
                'verbose_name': 'Program',
                'verbose_name_plural': 'Program',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('name_ar', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_project', to='users.user')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='managed_project', to='users.user')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='projects.program')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.projectpriority')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.projectstatus')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Project',
            },
        ),
        migrations.CreateModel(
            name='ProjectUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user')),
            ],
            options={
                'verbose_name': 'Project User',
                'verbose_name_plural': 'Project User',
                'unique_together': {('project', 'user', 'role')},
            },
        ),
    ]
