from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import * 

# Create your views here.
def home (request):
    return render(request, "home.html")





#----- CRUD TABLE ALUNO 

def createAluno (request):
    form = AlunoForm(request.POST or None)
    if form.is_valid() :
        form.save()
        return redirect("/readalunos") #mudar

    conteudo = {"formulario": form}
    return render(request, 'create_aluno.html', conteudo)


def readAluno (request):
    aluno = Aluno.objects.all()
    conteudo = {"alunos":aluno}

    return render(request,'crud_alunos.html', conteudo)


def updateAluno (request, id):
    aluno = Aluno.objects.get(pk=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid() :
        form.save()
        return redirect("/readalunos") #mudar

    conteudo = {"formulario": form}
    return render(request, 'create_aluno.html', conteudo)


def deleteAluno(request,id):
    aluno = Aluno.objects.get(pk=id)
    aluno.delete()
    return redirect("/readalunos")


#------CRUD TABELA CURSO

def createCurso (request):
    form = CursoForm(request.POST or None)
    if form.is_valid() :
        form.save()
        return redirect("/readcursos") 

    conteudo = {"curso": form}
    return render(request, 'create_curso.html', conteudo)