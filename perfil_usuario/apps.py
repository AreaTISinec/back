from django.apps import AppConfig


class PerfilUsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil_usuario'

    def ready(self):
        import perfil_usuario.signals
