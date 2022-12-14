from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome')
    list_display_links = ('id', 'nome')
    list_filter = ('nome', 'sobrenome')
    search_fields = ('nome', 'sobrenome')

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)