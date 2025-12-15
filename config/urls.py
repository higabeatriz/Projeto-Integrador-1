from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views
from core.views import MedicamentoViewSet, IntervencaoViewSet, PerfilPacienteViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

router = DefaultRouter()
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'pacientes', PerfilPacienteViewSet)
router.register(r'intervencoes', IntervencaoViewSet, basename='intervencao')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', auth_views.obtain_auth_token),
    
    
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Documentação Interativa
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'), # Documentação Formal

] 