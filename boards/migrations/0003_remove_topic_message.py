# Generated by Django 2.1.1 on 2018-09-26 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_topic_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='message',
        ),
    ]
