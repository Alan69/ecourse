# Generated by Django 3.0.5 on 2022-06-18 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_teachercourse_link_to_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachercourse',
            name='author',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='teachercourse',
            name='author_info',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
