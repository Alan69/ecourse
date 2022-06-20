from email import message
from turtle import pos
from unicodedata import category
from django.shortcuts import render, redirect
from matplotlib.style import context
from .models import Category, Post, CategoryName, CategoryCs, CategoryLego, TeacherCourse
from .forms import MyForm, MyForm2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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

def teachersingle(request, pk):
    category = TeacherCourse.objects.get(id = pk)
    cat_name = CategoryName.objects.all()
    return render(request, 'teachersingle.html', {'cat_name': cat_name, 'category':category})

def teacherCourseShow(request):
    category = TeacherCourse.objects.all()
    return render(request, 'teachercourseshow.html', {'category':category})

def teacherCourseAdd(request):
    form = MyForm2(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
    return render(request, 'teacheraddcourse.html', context)

def registerForm(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {"form":form}
    return render(request, "register.html", context)

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            return redirect('teacheraddcourse')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, "login.html", context)

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