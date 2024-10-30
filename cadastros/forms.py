from django import forms
from .models import Turma, Aluno, Educador

class TurmaForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'horario']

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'email', 'matricula', 'data_nascimento', 'contato_pais', 'endereco', 'data_entrada_programa', 'data_saida_programa', 'necessidade_especial', 'detalhes_necessidade_especial', 'turma']

class EducadorForm(forms.ModelForm):
    class Meta:
        model = Educador
        fields = ['nome', 'formacao', 'contato', 'modalidade', 'turma_responsavel']
