from django.contrib import admin
from .models import Category, CategoryName, Post, CategoryCs, CategoryLego
# Register your models here.

admin.site.register(Category)
admin.site.register(CategoryCs)
admin.site.register(CategoryName)
admin.site.register(Post)
admin.site.register(CategoryLego)

