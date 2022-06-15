from turtle import pos
from unicodedata import category
from django.shortcuts import render
from .models import Category, Post, CategoryName, CategoryCs, CategoryLego
from .forms import MyForm

def main(request):
    category = Category.objects.all()
    return render(request, 'index.html', {'category':category})

def single(request, pk):
    category = Category.objects.get(id = pk)
    cat_name = CategoryName.objects.all()
    return render(request, 'single.html', {'cat_name': cat_name, 'category':category})

def single2(request, pk):
    category = CategoryCs.objects.get(id = pk)
    cat_name = CategoryName.objects.all()
    return render(request, 'single2.html', {'cat_name': cat_name, 'category':category})

def single3(request, pk):
    category = CategoryLego.objects.get(id = pk)
    cat_name = CategoryName.objects.all()
    return render(request, 'single3.html', {'cat_name': cat_name, 'category':category})

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = MyForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
    return render(request, 'contact.html', context)

def course(request):
    category = Category.objects.all()
    return render(request, 'course.html', {'category':category})

def python(request):
    category = Category.objects.all()
    return render(request, 'python.html', {'category':category})

def csharp(request):
    category = CategoryCs.objects.all()
    return render(request, 'csharp.html', {'category':category})

def lego(request):
    category = CategoryLego.objects.all()
    return render(request, 'lego.html', {'category':category})

def teacher(request):
    return render(request, 'teacher.html')