from django.contrib import admin
from .models import Evento, Categoria, Localizacao

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("data_inicio", "data_fim", "gasto")

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("designacao",)

@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    list_display = ("localidade", "rua", "cod_postal", "capacidade")