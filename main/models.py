import email
from statistics import mode
from django.db import models
from matplotlib.pyplot import cla

class CategoryName(models.Model):
    catefory_name = models.CharField(max_length=255, default="Web development")

    def __str__(self):
        return self.catefory_name

# Create your models here.
class Category(models.Model):
    image_name = models.ImageField(upload_to='static/main/img')
    
    topic = models.CharField(max_length=255) # and lesson number
    link_to_youtube = models.CharField(max_length=255)
    about_topic = models.TextField()
    under_topic = models.CharField(max_length=255)
    lesson_image_name = models.ImageField(upload_to="media/")
    lesson_text = models.TextField()

    def __str__(self):
        return self.topic

class CategoryCs(models.Model):
    image_name = models.ImageField(upload_to='static/main/img')
    
    topic = models.CharField(max_length=255)
    link_to_youtube = models.CharField(max_length=255)
    about_topic = models.TextField()
    under_topic = models.CharField(max_length=255)
    lesson_image_name = models.ImageField(upload_to="media/")
    lesson_text = models.TextField()

    def __str__(self):
        return self.topic

class CategoryLego(models.Model):
    image_name = models.ImageField(upload_to='static/main/img')
    
    topic = models.CharField(max_length=255)
    link_to_youtube = models.CharField(max_length=255)
    about_topic = models.TextField()
    under_topic = models.CharField(max_length=255)
    lesson_image_name = models.ImageField(upload_to="media/")
    lesson_text = models.TextField()

    def __str__(self):
        return self.topic

class Post(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

