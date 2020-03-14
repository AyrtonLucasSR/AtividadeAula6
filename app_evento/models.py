from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Pessoa(models.Model):
	nome= models.CharField('Nome',max_length=128)
	email= models.EmailField('E-mail', null=True, blank=True)

	def _str_(self):
		return self.nome


class PessoaFisica(models.Model):
	pessoa=models.ForeignKey(Pessoa, on_delete=models.CASCADE,blank=True,null=True)
	cpf=models.CharField('CPF', max_length=15,
		help_text='Número do cpf no formato 00000000000',null=True,
		blank=True,)

	def _str_(self):
		return self.cpf

class Evento(models.Model):
    nome = models.CharField('nome',max_length = 50)
    sigla = models.CharField('Sigla',max_length = 50)
    data_icinio = models.DateTimeField(default=timezone.now)
    realizador=models.ForeignKey(Pessoa, on_delete=models.CASCADE,blank=True,null=True)
    descricao = models.TextField()

    def _str_(self):
        return self.sigla

class Ingresso(models.Model):
    descricao = models.CharField('nome',max_length=128)
    valor=models.TextField()
    evento= models.ForeignKey(Evento, on_delete=models.CASCADE,blank=True, null=True)
	
    def _str_(self):
        return self.descricao

class Inscricao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,blank=True, null=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE,blank=True, null=True)
    ingresso= models.ForeignKey(Ingresso, on_delete=models.CASCADE,blank=True, null=True)



# Create your models here.
