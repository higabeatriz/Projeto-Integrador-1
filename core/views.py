from rest_framework import viewsets
from .models import Medicamento, Intervencao, PerfilPaciente
from .serializers import MedicamentoSerializer, IntervencaoSerializer, PerfilPacienteSerializer
from .permissions import IsFarmaceutico, IsPacienteOwnerOrFarmaceutico

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
    # Apenas Farmacêuticos podem mexer em medicamentos
    permission_classes = [IsFarmaceutico]

class PerfilPacienteViewSet(viewsets.ModelViewSet):
    queryset = PerfilPaciente.objects.all()
    serializer_class = PerfilPacienteSerializer
    permission_classes = [IsFarmaceutico]

class IntervencaoViewSet(viewsets.ModelViewSet):
    serializer_class = IntervencaoSerializer
    permission_classes = [IsPacienteOwnerOrFarmaceutico]

    def get_queryset(self):
        user = self.request.user
        # Se for Farmacêutico ou Superusuário, vê tudo
        if user.is_superuser or user.groups.filter(name='Farmacêuiticos').exists():
            return Intervencao.objects.all()
        # Se for Paciente, vê só as suas
        if hasattr(user, 'perfil_paciente'):
            return Intervencao.objects.filter(paciente__user=user)
        return Intervencao.objects.none()

    def perform_create(self, serializer):
        # Assina automaticamente com seu nome
        serializer.save(farmaceutico=self.request.user)