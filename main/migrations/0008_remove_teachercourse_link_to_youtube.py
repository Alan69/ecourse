# Generated by Django 3.0.5 on 2022-06-18 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_teachercourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teachercourse',
            name='link_to_youtube',
        ),
    ]
