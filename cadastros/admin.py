from django.contrib import admin

from .models import Turma, Educador, Aluno, Frequencia

# Register your models here.
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Educador)

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    list_display = ['data', 'aluno', 'presenca']
    list_filter = ['data', 'presenca']
    search_fields = ['aluno__nome']
