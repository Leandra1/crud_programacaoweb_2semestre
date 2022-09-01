from django.http import HttpResponse
from django.shortcuts import render,redirect
from .form import * 

# Create your views here.
def teste (request):
    return HttpResponse("Aqui")





#----- CRUD TABLE ALUNO 

def CreateAluno (request):
    form = AlunoForm(request.POST or None)
    if form.is_valid() :
        form.save()
        return redirect("/teste") #mudar

    conteudo = {"formulario": form}
    return render(request, 'create_aluno.html', conteudo)







#------CRUD TABELA CURSO

def CreateCurso (request):
    form = CursoForm(request.POST or None)
    if form.is_valid() :
        form.save()
        return redirect("/teste") #mudar

    conteudo = {"curso": form}
    return render(request, 'create_curso.html', conteudo)