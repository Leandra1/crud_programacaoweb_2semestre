from django.forms import ModelForm
from .models import Aluno, Curso

class AlunoForm (ModelForm):
    
    class Meta:
        model = Aluno
        fields = ('cpf','nome','email','fone','data_nascimento')


class CursoForm (ModelForm):

    class Meta:
        model = Curso
        fields = ('nome', 'requisito', 'carga_horaria', 'preco')