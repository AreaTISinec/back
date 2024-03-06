from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import UserAccount
from  .models import UserProfile


@receiver(post_save, sender=UserAccount)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        id_user = instance.id
        print(id_user)
        username = instance.username
        profile = UserProfile(user_id=id_user, nombre=username, apellido='', numero='', empresa_id=1)
        profile.save()