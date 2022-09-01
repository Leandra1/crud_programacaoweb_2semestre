from django.forms import ModelForm
from .models import Aluno, Curso
from django.forms.widgets import NumberInput

class AlunoForm (ModelForm):
    
    class Meta:
        model = Aluno
        fields = ('cpf','nome','email','fone','data_nascimento')
        widgets = {
            'data_nascimento' : NumberInput(attrs={'type':'date'})
        }


class CursoForm (ModelForm):

    class Meta:
        model = Curso
        fields = ('nome', 'requisito', 'carga_horaria', 'preco')