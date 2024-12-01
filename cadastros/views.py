from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Turma, Aluno, Educador
from .forms import TurmaForm, AlunoForm, EducadorForm

# Turma CRUD
class TurmaListView(LoginRequiredMixin, ListView):
    model = Turma
    template_name = 'turma/turma_list.html'
    context_object_name = 'turmas'

class TurmaCreateView(LoginRequiredMixin, CreateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'turma/turma_form.html'
    success_url = reverse_lazy('turma_list')

class TurmaUpdateView(LoginRequiredMixin, UpdateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'turma/turma_form.html'
    success_url = reverse_lazy('turma_list')

class TurmaDeleteView(LoginRequiredMixin, DeleteView):
    model = Turma
    template_name = 'turma/turma_confirm_delete.html'
    success_url = reverse_lazy('turma_list')

# Aluno CRUD
class AlunoListView(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = 'aluno/aluno_list.html'
    context_object_name = 'alunos'

class AlunoCreateView(LoginRequiredMixin, CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'
    success_url = reverse_lazy('aluno_list')

class AlunoUpdateView(LoginRequiredMixin, UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'
    success_url = reverse_lazy('aluno_list')

class AlunoDeleteView(LoginRequiredMixin, DeleteView):
    model = Aluno
    template_name = 'aluno/aluno_confirm_delete.html'
    success_url = reverse_lazy('aluno_list')

# Educador CRUD
class EducadorListView(LoginRequiredMixin, ListView):
    model = Educador
    template_name = 'educador/educador_list.html'
    context_object_name = 'educadores'

class EducadorCreateView(LoginRequiredMixin, CreateView):
    model = Educador
    form_class = EducadorForm
    template_name = 'educador/educador_form.html'
    success_url = reverse_lazy('educador_list')

class EducadorUpdateView(LoginRequiredMixin, UpdateView):
    model = Educador
    form_class = EducadorForm
    template_name = 'educador/educador_form.html'
    success_url = reverse_lazy('educador_list')

class EducadorDeleteView(LoginRequiredMixin, DeleteView):
    model = Educador
    template_name = 'educador/educador_confirm_delete.html'
    success_url = reverse_lazy('educador_list')

