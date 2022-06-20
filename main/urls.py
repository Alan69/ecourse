from xml.dom.minidom import Document
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('single/<int:pk>/', views.single, name='single'),
    path('single2/<int:pk>/', views.single2, name='single2'),
    path('single3/<int:pk>/', views.single3, name='single3'),
    path('teachersingle/<int:pk>/', views.teachersingle, name='teachersingle'),
    path('register/', views.registerForm, name='register'),
    path('login/', views.loginPage, name='login'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('teacheraddcourse/', views.teacherCourseAdd, name='teacheraddcourse'),
    path('teacher/', views.teacher, name='teacher'),
    path('course/', views.course, name='course'),
    path('python/', views.python, name='python'),
    path('csharp/', views.csharp, name='csharp'),
    path('lego/', views.lego, name='lego'),
    path('teacherCourseShow/', views.teacherCourseShow, name='teacherCourseShow'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 