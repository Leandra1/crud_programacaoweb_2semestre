"""Ava_Crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Crud.views import * 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('createaluno/', createAluno, name="adicionaraluno"),
    path('readalunos/', readAluno, name="listaralunos"),
    path('updatealunos/<int:id>', updateAluno, name="updatealunos"),
    path('deletealunos/<int:id>', deleteAluno, name="deletea"),


    path('createcurso/', createCurso, name="adicionarcurso"),
    path('listagemcurso/', listagem, name="listagemcurso"),
    path('componentes/', componentes, name="componentes"),
    
    path('', home, name="home"),
]
