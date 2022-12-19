from django.db import models

# Create your models here.

class Aluno (models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    fone = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Instrutor (models.Model):
     id = models.AutoField(primary_key=True)
     nome = models.CharField(max_length=50)
     email = models.EmailField(max_length=50)
     valor_hora = models.IntegerField()
     certificados = models.CharField(max_length=255)

     def __str__(self):
        return self.nome


class Curso (models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    requisito = models.CharField(max_length=255)
    carga_horaria = models.SmallIntegerField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome


class Turma (models.Model):
    id = models.AutoField(primary_key=True)
    data_inicio = models.DateField()
    data_final = models.DateField()
    carga_horaria = models.SmallIntegerField()
    instrutor_id = models.ForeignKey(Instrutor, on_delete = models.CASCADE)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE)


class Matricula (models.Model):
    id = models.AutoField(primary_key=True)
    data_matricula = models.DateField()
    turma_id = models.ForeignKey(Turma, on_delete=models.CASCADE)
    aluno_id = models.ForeignKey(Aluno, on_delete=models.CASCADE)