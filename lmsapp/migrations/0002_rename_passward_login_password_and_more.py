# Generated by Django 4.2.4 on 2023-09-09 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lmsapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='passward',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='emailaddess',
            new_name='emailaddress',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='regrate',
            new_name='regdate',
        ),
    ]
