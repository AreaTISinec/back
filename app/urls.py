from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import CustomTokenObtainPairView

schema_view = get_schema_view(
   openapi.Info(
      title="SGO API",
      default_version='v1',
      description="Documentacion de la API del sistema SGO",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ldroguett@sinec.cl"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/accounts/', include('accounts.urls')),
    path('api/ventas/', include('ventas.urls')),
    path('api/obras/', include('obras.urls')),
    path('api/cene/', include('cene.urls')),
    path('api/avance/', include('avance.urls')),
    path('api/files/', include('files.urls')),
    path('api/powerbi/', include('powerbi.urls')),
    path('api/estados-obra/', include('estado_obras.urls')),
    path('api/tipos-obra/', include('tipo_obras.urls')),
    path('api/empresas/', include('empresas.urls')),
    path('api/cliente/', include('clientes.urls')),
    path('admin/', admin.site.urls),
    path('api/asignacion/', include('asignaciones.urls')),
    path('api/historial/', include('historial_financiero.urls')),
    path('api/profile/', include('perfil_usuario.urls')),
    
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] 
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

