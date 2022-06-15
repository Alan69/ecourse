# Generated by Django 3.0.5 on 2022-06-07 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_category_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.ImageField(upload_to='static/main/img')),
                ('topic', models.CharField(max_length=255)),
                ('link_to_youtube', models.CharField(default='https://www.youtube.com/embed/MrmbEH5ti84', max_length=255)),
                ('about_topic', models.TextField()),
                ('under_topic', models.CharField(max_length=255)),
                ('lesson_image_name', models.ImageField(upload_to='media/')),
                ('lesson_text', models.TextField()),
            ],
        ),
    ]
