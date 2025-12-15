from django.db import models
from django.contrib.auth.models import User

# --- 1. Perfil do Paciente ---
class PerfilPaciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_paciente')
    nome_completo = models.CharField(max_length=100, help_text="Nome completo do paciente")
    prontuario = models.CharField(max_length=20, unique=True, help_text="Número do registro hospitalar")
    data_nascimento = models.DateField(null=True, blank=True)
    leito = models.CharField(max_length=20, help_text="Ex: UTI-01, Enf-204")
    alergias = models.TextField(blank=True, help_text="Liste as alergias conhecidas")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return f"{self.nome_completo} ({self.leito})"

# --- 2. Medicamento ---
class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    principio_ativo = models.CharField(max_length=100, blank=True, null=True)
    concentracao = models.CharField(max_length=50, blank=True, null=True, help_text="Ex: 500mg, 1g")

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"

    def __str__(self):
        return f"{self.nome} {self.concentracao or ''}"

# --- 3. Intervenção ---
class Intervencao(models.Model):
    PROBLEMA_CHOICES = [
        ('SOBREDOSAGEM', 'Sobredosagem / Dose Alta'),
        ('SUBDOSAGEM', 'Subdosagem / Dose Baixa'),
        ('DUPLICIDADE', 'Duplicidade Terapêutica'),
        ('INTERACAO', 'Interação Medicamentosa'),
        ('REACAO_ADVERSA', 'Reação Adversa (RAM)'),
        ('VIA_INADEQUADA', 'Via de Administração Inadequada'),
        ('DILUICAO_INCOMPATIVEL', 'Diluição/Estabilidade Incompatível'),
        ('SEM_INDICACAO', 'Medicamento sem Indicação'),
        ('OMISSAO', 'Omissão de Dose / Medicamento Faltando'),
        ('ALERGIA', 'Paciente com Alergia Conhecida'),
        ('OUTRO', 'Outro'),
    ]

    ACEITACAO_CHOICES = [
        ('PENDENTE', 'Aguardando Resposta'),
        ('ACEITA', 'Intervenção Aceita'),
        ('NAO_ACEITA', 'Não Aceita'),
        ('ACEITA_PARCIAL', 'Aceita Parcialmente'),
    ]

    paciente = models.ForeignKey(PerfilPaciente, on_delete=models.CASCADE, related_name='intervencoes')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    farmaceutico = models.ForeignKey(User, on_delete=models.CASCADE, related_name='intervencoes_realizadas')
    
    data_registro = models.DateTimeField(auto_now_add=True)
    tipo_problema = models.CharField(max_length=30, choices=PROBLEMA_CHOICES, default='OUTRO')
    descricao_problema = models.TextField(help_text="Descreva brevemente o que ocorreu.")
    conduta_proposta = models.TextField(help_text="O que você sugeriu ao médico?")
    aceitacao = models.CharField(max_length=20, choices=ACEITACAO_CHOICES, default='PENDENTE')

    class Meta:
        verbose_name = "Intervenção"
        verbose_name_plural = "Intervenções"

    def __str__(self):
        return f"{self.get_tipo_problema_display()} - {self.paciente.nome_completo}"