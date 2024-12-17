from django.urls import path
from .views import (
    TurmaListView, TurmaCreateView, TurmaUpdateView, TurmaDeleteView,
    AlunoListView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView,
    EducadorListView, EducadorCreateView, EducadorUpdateView, EducadorDeleteView, 
    AulaListView, AulaCreateView, AulaUpdateView, AulaDeleteView, 
    FrequenciaCreateView, FrequenciaListView, FrequenciaUpdateView, FrequenciaDeleteView
)

urlpatterns = [
    # Turma URLs
    path('turmas/', TurmaListView.as_view(), name='turma_list'),
    path('turmas/create/', TurmaCreateView.as_view(), name='turma_create'),
    path('turmas/update/<int:pk>/', TurmaUpdateView.as_view(), name='turma_update'),
    path('turmas/delete/<int:pk>/', TurmaDeleteView.as_view(), name='turma_delete'),

    # Aluno URLs
    path('alunos/', AlunoListView.as_view(), name='aluno_list'),
    path('alunos/create/', AlunoCreateView.as_view(), name='aluno_create'),
    path('alunos/update/<int:pk>/', AlunoUpdateView.as_view(), name='aluno_update'),
    path('alunos/delete/<int:pk>/', AlunoDeleteView.as_view(), name='aluno_delete'),

    # Educador URLs
    path('educadores/', EducadorListView.as_view(), name='educador_list'),
    path('educadores/create/', EducadorCreateView.as_view(), name='educador_create'),
    path('educadores/update/<int:pk>/', EducadorUpdateView.as_view(), name='educador_update'),
    path('educadores/delete/<int:pk>/', EducadorDeleteView.as_view(), name='educador_delete'),

    path('turmas/', TurmaListView.as_view(), name='turma_list'),
    path('alunos/', AlunoListView.as_view(), name='aluno_list'),
    path('educadores/', EducadorListView.as_view(), name='educador_list'),

    # Aula URLs
    path('aulas/', AulaListView.as_view(), name='aula_list'),
    path('aulas/create/', AulaCreateView.as_view(), name='aula_create'),
    path('aulas/update/<int:pk>/', AulaUpdateView.as_view(), name='aula_update'),
    path('aulas/delete/<int:pk>/', AulaDeleteView.as_view(), name='aula_delete'),

    # Fequencia URLs
    path('frequencias/', FrequenciaListView.as_view(), name='frequencia_list'),
    path('frequencias/adicionar/', FrequenciaCreateView.as_view(), name='frequencia_add'),
    path('frequencias/<int:pk>/editar/', FrequenciaUpdateView.as_view(), name='frequencia_edit'),
    path('frequencias/<int:pk>/excluir/', FrequenciaDeleteView.as_view(), name='frequencia_delete'),
]
