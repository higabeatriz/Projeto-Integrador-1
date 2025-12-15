from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PerfilPaciente, Medicamento, Intervencao

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PerfilPacienteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = PerfilPaciente
        fields = '__all__' 

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class IntervencaoSerializer(serializers.ModelSerializer):

    paciente_nome = serializers.CharField(source='paciente.nome_completo', read_only=True)
    leito_paciente = serializers.CharField(source='paciente.leito', read_only=True)
    medicamento_nome = serializers.CharField(source='medicamento.nome', read_only=True)
    farmaceutico_nome = serializers.CharField(source='farmaceutico.username', read_only=True)
    
    tipo_problema_descricao = serializers.CharField(source='get_tipo_problema_display', read_only=True)
    aceitacao_descricao = serializers.CharField(source='get_aceitacao_display', read_only=True)

    class Meta:
        model = Intervencao
        fields = '__all__'
        read_only_fields = ['farmaceutico']