# Generated by Django 4.2.4 on 2023-09-16 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_branch_program_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstore',
            name='year',
            field=models.CharField(default='hi', max_length=100),
            preserve_default=False,
        ),
    ]
