from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length = 60)
    data_de_nascimento = models.DateField()
    idade = models.IntegerField()
    especialidade = models.CharField(max_length = 50)
    bio = models.TextField()

    def __str__(self):
        return(self.nome + ' ' + self.sobrenome)

class Paciente(models.Model):
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)
    data_de_nascimento = models.DateField()
    idade = models.IntegerField()
    sintomas = models.TextField()

    def __str__(self):
        return(self.nome + ' ' + self.sobrenome)

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    funcao = models.TextField()
    def __str__(self):
        return(self.nome)

class Enfermidade(models.Model):
    nome = models.CharField(max_length=100)
    sintomas = models.TextField()
    medicamentos = models.TextField()
    def __str__(self):
        return(self.nome)

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    substancia = models.CharField(max_length=100)
    validade = models.DateField()
    contraindicacao = models.TextField()
    def __str__(self):
        return(self.nome)