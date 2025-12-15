import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('principio_ativo', models.CharField(blank=True, max_length=100, null=True)),
                ('concentracao', models.CharField(blank=True, help_text='Ex: 500mg, 1g', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PerfilPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(help_text='Nome completo do paciente', max_length=100)),
                ('prontuario', models.CharField(help_text='Número do registro hospitalar', max_length=20, unique=True)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('leito', models.CharField(help_text='Ex: UTI-01, Enf-204', max_length=20)),
                ('alergias', models.TextField(blank=True, help_text='Liste as alergias conhecidas')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_paciente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intervencao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_registro', models.DateTimeField(auto_now_add=True)),
                ('tipo_problema', models.CharField(choices=[('SOBREDOSAGEM', 'Sobredosagem / Dose Alta'), ('SUBDOSAGEM', 'Subdosagem / Dose Baixa'), ('DUPLICIDADE', 'Duplicidade Terapêutica'), ('INTERACAO', 'Interação Medicamentosa'), ('REACAO_ADVERSA', 'Reação Adversa (RAM)'), ('VIA_INADEQUADA', 'Via de Administração Inadequada'), ('DILUICAO_INCOMPATIVEL', 'Diluição/Estabilidade Incompatível'), ('SEM_INDICACAO', 'Medicamento sem Indicação'), ('OMISSAO', 'Omissão de Dose / Medicamento Faltando'), ('ALERGIA', 'Paciente com Alergia Conhecida'), ('OUTRO', 'Outro')], default='OUTRO', max_length=30)),
                ('descricao_problema', models.TextField(help_text='Descreva brevemente o que ocorreu.')),
                ('conduta_proposta', models.TextField(help_text='O que você sugeriu ao médico?')),
                ('aceitacao', models.CharField(choices=[('PENDENTE', 'Aguardando Resposta'), ('ACEITA', 'Intervenção Aceita'), ('NAO_ACEITA', 'Não Aceita'), ('ACEITA_PARCIAL', 'Aceita Parcialmente')], default='PENDENTE', max_length=20)),
                ('farmaceutico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intervencoes_realizadas', to=settings.AUTH_USER_MODEL)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.medicamento')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intervencoes', to='core.perfilpaciente')),
            ],
        ),
    ]
