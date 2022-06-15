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
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('teacher/', views.teacher, name='teacher'),
    path('course/', views.course, name='course'),
    path('python/', views.python, name='python'),
    path('csharp/', views.csharp, name='csharp'),
    path('lego/', views.lego, name='lego'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 