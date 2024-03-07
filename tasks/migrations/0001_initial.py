# Generated by Django 5.0 on 2024-03-07 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('title_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(max_length=7)),
                ('due_date', models.DateTimeField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('estimated_hours', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('actual_hours', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_hidden', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Task',
            },
        ),
        migrations.CreateModel(
            name='TaskAssignment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaskAttachement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='attachments_tasks/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskCommentAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='attachments_commnets/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskPriority',
            fields=[
                ('priority_id', models.AutoField(primary_key=True, serialize=False)),
                ('priority', models.CharField(max_length=50)),
                ('priority_ar', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(max_length=7)),
            ],
            options={
                'verbose_name': 'Task Priority',
                'verbose_name_plural': 'Task Priority',
            },
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=50)),
                ('status_ar', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(max_length=7)),
            ],
            options={
                'verbose_name': 'Task Status',
                'verbose_name_plural': 'Task Status',
            },
        ),
        migrations.CreateModel(
            name='TaskTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
