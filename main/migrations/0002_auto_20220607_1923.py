# Generated by Django 3.0.5 on 2022-06-07 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='main_image_name',
        ),
        migrations.AddField(
            model_name='category',
            name='link_to_youtube',
            field=models.CharField(default='https://www.youtube.com/embed/9ue4NtiS53k', max_length=255),
        ),
    ]