# Generated by Django 3.2.5 on 2021-07-14 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_quiz_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='duration',
        ),
    ]
