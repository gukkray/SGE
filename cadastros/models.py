from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth.models import User


class Turma(models.Model):
    HORARIO_CHOICES = [
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Noturno', 'Noturno'),
    ]

    nome = models.CharField(max_length=100)  # Nome da turma
    horario = models.CharField(
        max_length=10,
        choices=HORARIO_CHOICES,
        default='Matutino'
    )  # Horário da turma

    def __str__(self):
        return f"Turma {self.nome} - Horário: {self.horario}"


class Aluno(models.Model):
    nome = models.CharField(max_length=100)  # Nome do aluno
    idade = models.IntegerField()  # Idade do aluno
    email = models.EmailField(unique=True)  # Email do aluno
    matricula = models.CharField(max_length=20, unique=True)  # Número de matrícula
    data_matricula = models.DateField(auto_now_add=True)  # Data de matrícula (preenchido automaticamente)

    # Campos adicionais solicitados
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", default="2000-01-01")# Data de aniversário
    contato_pais = models.CharField(max_length=200, verbose_name="Contato dos Pais", default="N/A")
    endereco = models.TextField(verbose_name="Endereço", default="N/A")  # Endereço do aluno
    data_entrada_programa = models.DateField(verbose_name="Data de Entrada no Programa", default=timezone.now)  # Data de entrada no programa
    data_saida_programa = models.DateField(
        verbose_name="Data de Saída do Programa",
        null=True,
        blank=True
    )  # Data de saída do programa (opcional)

    # Campo para necessidade especial
    necessidade_especial = models.BooleanField(default=False, verbose_name="Necessidade Especial")  # Indica se o aluno tem necessidade especial
    detalhes_necessidade_especial = models.TextField(
        blank=True,
        null=True,
        verbose_name="Detalhes da Necessidade Especial"
    )  # Detalhes opcionais sobre a necessidade especial, caso aplicável

    # Relacionamento com a turma (um aluno só pode estar em uma turma)
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE, related_name='alunos')

    def __str__(self):
        return f"{self.nome} ({self.matricula})"


class Educador(models.Model):
    nome = models.CharField(max_length=100)  # Nome completo do educador
    formacao = models.CharField(max_length=200)  # Formação acadêmica ou profissional
    contato = models.CharField(max_length=50)  # Informações de contato (telefone, email, etc.)
    modalidade = models.CharField(max_length=100)  # Modalidade em que o educador atua no programa (ex: esportes, artes, etc.)

    # Campo adicional solicitado
    turma_responsavel = models.ForeignKey(
        'Turma',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='educadores_responsaveis',
        verbose_name="Turma Responsável"
    )  # Turma que o educador está responsável

    def __str__(self):
        return f"Educador: {self.nome} - Modalidade: {self.modalidade}"

class Aula(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título da Aula")
    descricao = models.TextField(verbose_name="Descrição")
    data_hora = models.DateTimeField(verbose_name="Data e Hora")
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name="aulas")
    educador = models.ForeignKey(Educador, on_delete=models.SET_NULL, null=True, related_name="aulas")

    def __str__(self):
        return f"{self.titulo} - {self.turma.nome} ({self.data_hora.strftime('%d/%m/%Y %H:%M')})"
