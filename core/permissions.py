from rest_framework import permissions

class IsFarmaceutico(permissions.BasePermission):
    """
    Permite acesso total apenas se o usuário pertencer ao grupo 'Farmacêuticos'.
    """
    def has_permission(self, request, view):
        # Superusuário ou membro do grupo Farmacêuticos pode tudo
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Farmacêuticos').exists()

class IsPacienteOwnerOrFarmaceutico(permissions.BasePermission):
    """
    Farmacêuticos: Veem tudo e editam tudo.
    Pacientes: Veem apenas seus próprios dados (Leitura).
    """
    def has_permission(self, request, view):
        # O usuário tem que estar logado
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Se for superusuário ou farmacêutico, libera tudo
        if request.user.is_superuser or request.user.groups.filter(name='Farmacêuticos').exists():
            return True
        
        # Se for paciente, só libera se for leitura (GET) E se o dado for dele
        if request.method in permissions.SAFE_METHODS:
            # Verifica se o objeto tem o campo 'user' (PerfilPaciente)
            if hasattr(obj, 'user'): 
                return obj.user == request.user
            # Verifica se o objeto tem o campo 'paciente' (Intervencao)
            if hasattr(obj, 'paciente'): 
                return obj.paciente.user == request.user
        
        return False