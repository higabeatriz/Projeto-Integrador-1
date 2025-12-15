from django.contrib import admin
from .models import PerfilPaciente, Medicamento, Intervencao

# Tabelas no admin do Django
admin.site.register(PerfilPaciente)
admin.site.register(Medicamento)
admin.site.register(Intervencao)