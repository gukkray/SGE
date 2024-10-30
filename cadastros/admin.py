from django.contrib import admin

from .models import Turma, Educador, Aluno

# Register your models here.
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Educador)

