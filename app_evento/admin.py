from django.contrib import admin
from .models import Evento, Pessoa, PessoaFisica, Inscricao, Ingresso

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass
@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
	pass
@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
	pass
@admin.register(Inscricao)
class InscricaoAdmin(admin.ModelAdmin):
	pass
@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
	pass
# Register your models here.
