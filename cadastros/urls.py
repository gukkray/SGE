from django.urls import path
from .views import (
    TurmaListView, TurmaCreateView, TurmaUpdateView, TurmaDeleteView,
    AlunoListView, AlunoCreateView, AlunoUpdateView, AlunoDeleteView,
    EducadorListView, EducadorCreateView, EducadorUpdateView, EducadorDeleteView, 
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
]
