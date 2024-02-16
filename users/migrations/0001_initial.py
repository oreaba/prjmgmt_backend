# Generated by Django 5.0.2 on 2024-02-16 04:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=50)),
                ('role_ar', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('firstname_ar', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100)),
                ('title_ar', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('extension', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
            },
        ),
        migrations.CreateModel(
            name='RoleDuty',
            fields=[
                ('duty_id', models.AutoField(primary_key=True, serialize=False)),
                ('duty', models.CharField(max_length=100)),
                ('duty_ar', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.role')),
            ],
            options={
                'verbose_name': 'Role Duty',
                'verbose_name_plural': 'Role Duty',
            },
        ),
    ]
