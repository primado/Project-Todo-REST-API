# Generated by Django 3.2 on 2023-10-23 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='user',
            new_name='username',
        ),
    ]
