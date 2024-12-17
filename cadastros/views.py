from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Turma, Aluno, Educador, Aula, Frequencia
from .forms import TurmaForm, AlunoForm, EducadorForm, AulaForm, FrequenciaForm

# Views para Turma
class TurmaCreateView(PermissionRequiredMixin, CreateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'turma/turma_form.html'
    success_url = reverse_lazy('turma_list')
    permission_required = 'cadastros.add_turma'

class TurmaListView(PermissionRequiredMixin, ListView):
    model = Turma
    template_name = 'turma/turma_list.html'
    context_object_name = 'turmas'
    permission_required = 'cadastros.view_turma'


class TurmaUpdateView(PermissionRequiredMixin, UpdateView):
    model = Turma
    form_class = TurmaForm
    template_name = 'turma/turma_form.html'
    success_url = reverse_lazy('turma_list')
    permission_required = 'cadastros.change_turma'

class TurmaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Turma
    template_name = 'turma/turma_confirm_delete.html'
    success_url = reverse_lazy('turma_list')
    permission_required = 'cadastros.delete_turma'

# Views para Aluno
class AlunoCreateView(PermissionRequiredMixin, CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'
    success_url = reverse_lazy('aluno_list')
    permission_required = 'cadastros.add_aluno'

class AlunoListView(PermissionRequiredMixin, ListView):
    model = Aluno
    template_name = 'aluno/aluno_list.html'
    context_object_name = 'alunos'
    permission_required = 'cadastros.view_aluno'
    

class AlunoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'aluno/aluno_form.html'
    success_url = reverse_lazy('aluno_list')
    permission_required = 'cadastros.change_aluno'

class AlunoDeleteView(PermissionRequiredMixin, DeleteView):
    model = Aluno
    template_name = 'aluno/aluno_confirm_delete.html'
    success_url = reverse_lazy('aluno_list')
    permission_required = 'cadastros.delete_aluno'

# Views para Educador
class EducadorCreateView(PermissionRequiredMixin, CreateView):
    model = Educador
    form_class = EducadorForm
    template_name = 'educador/educador_form.html'
    success_url = reverse_lazy('educador_list')
    permission_required = 'cadastros.add_educador'

class EducadorListView(PermissionRequiredMixin, ListView):
    model = Educador
    template_name = 'educador/educador_list.html'
    context_object_name = 'educadores'
    permission_required = 'cadastros.view_educador'
 

class EducadorUpdateView(PermissionRequiredMixin, UpdateView):
    model = Educador
    form_class = EducadorForm
    template_name = 'educador/educador_form.html'
    success_url = reverse_lazy('educador_list')
    permission_required = 'cadastros.change_educador'

class EducadorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Educador
    template_name = 'educador/educador_confirm_delete.html'
    success_url = reverse_lazy('educador_list')
    permission_required = 'cadastros.delete_educador'

# Views para Aula
class AulaCreateView(PermissionRequiredMixin, CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'aula/aula_form.html'
    success_url = reverse_lazy('aula_list')
    permission_required = 'cadastros.add_aula'

class AulaListView(PermissionRequiredMixin, ListView):
    model = Aula
    template_name = 'aula/aula_list.html'
    context_object_name = 'aulas'
    permission_required = 'cadastros.view_aula'

class AulaUpdateView(PermissionRequiredMixin, UpdateView):
    model = Aula
    form_class = AulaForm
    template_name = 'aula/aula_form.html'
    success_url = reverse_lazy('aula_list')
    permission_required = 'cadastros.change_aula'

class AulaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Aula
    template_name = 'aula/aula_confirm_delete.html'
    success_url = reverse_lazy('aula_list')
    permission_required = 'cadastros.delete_aula'

# Views para Frequência
class FrequenciaCreateView(PermissionRequiredMixin, CreateView):
    model = Frequencia
    form_class = FrequenciaForm
    template_name = 'frequencia/frequencia_form.html'
    success_url = reverse_lazy('frequencia_list')
    permission_required = 'cadastros.add_frequencia'

class FrequenciaListView(PermissionRequiredMixin, ListView):
    model = Frequencia
    template_name = 'frequencia/frequencia_list.html'
    context_object_name = 'frequencias'
    permission_required = 'cadastros.view_frequencia'

class FrequenciaUpdateView(PermissionRequiredMixin, UpdateView):
    model = Frequencia
    form_class = FrequenciaForm
    template_name = 'frequencia/frequencia_form.html'
    success_url = reverse_lazy('frequencia_list')
    permission_required = 'cadastros.change_frequencia'

class FrequenciaDeleteView(PermissionRequiredMixin, DeleteView):
    model = Frequencia
    template_name = 'frequencia/frequencia_confirm_delete.html'
    success_url = reverse_lazy('frequencia_list')
    permission_required = 'cadastros.delete_frequencia'
