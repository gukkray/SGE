from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver
from cadastros.models import Turma, Aluno, Educador  # Substitua pelo caminho correto dos seus models

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    # Cria os grupos
    gestores_group, created = Group.objects.get_or_create(name='Gestores')
    educadores_group, created = Group.objects.get_or_create(name='Educadores')

    # Permissões para Gestores: acesso completo
    gestor_permissions = Permission.objects.filter(
        content_type__model__in=['turma', 'aluno', 'educador']
    )
    gestores_group.permissions.set(gestor_permissions)

    # Permissões para Educadores: adicionar e visualizar Turma e Aluno
    educador_permissions = Permission.objects.filter(
        codename__in=['add_turma', 'view_turma', 'add_aluno', 'view_aluno']
    )
    educadores_group.permissions.set(educador_permissions)

    print("Grupos e permissões configurados com sucesso!")
