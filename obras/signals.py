from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Max
from .models import  Obras
from avance.models import Avances
from files.models import File
from historial_financiero.models import Historial


@receiver(post_save, sender=Avances)
def actualizar_porcentaje_avance(sender, instance, created, **kwargs):
    if created:
        id_obra = instance.id_obra_id
        ultimo_avance_operacional = Avances.objects.filter(id_obra=id_obra, tipo='real').aggregate(Max('fecha'))
        if ultimo_avance_operacional['fecha__max']:
            ultimo_porcentaje = Avances.objects.filter(id_obra=id_obra, fecha=ultimo_avance_operacional['fecha__max']).last().porcentaje
            obra = Obras.objects.get(id=id_obra)
            obra.porc_avance_operativo = ultimo_porcentaje
            obra.save()
            # obra.update(porc_avance_operativo=ultimo_porcentaje)
            
        

@receiver(post_delete, sender=Avances)
def eliminar_actualizar_porcentaje_avance(sender, instance, **kwargs):
    id_obra = instance.id_obra_id
    print('antes del if')
    avances = Avances.objects.filter(id_obra=id_obra).order_by('-fecha')

    if avances.exists():
        print('dentro del if')
        ultimo_avance = avances.first()
        Obras.objects.filter(id=id_obra).update(porc_avance_operativo=ultimo_avance.porcentaje)
    else:
        # No hay avances, por lo que porcentaje de avance en Obras podría ser
        # actualizado a un valor por defecto o a None según la lógica de tu aplicación
        print('else signal')
        Obras.objects.filter(id=id_obra).update(porc_avance_operativo=0)
        
@receiver(post_save, sender=Avances)
def actualizar_is_avance(sender, instance, created, **kwargs):
    if created:  
        obra_id = instance.id_obra_id
        
        if instance.tipo == 'proyectado' and instance.porcentaje == 100:
            Obras.objects.filter(id=obra_id).update(is_avance=True)
        
    
        

@receiver(post_save, sender=File)
def actualizar_req_files(sender, instance, created, **kwargs):
    if created:
        obra = instance.id_obra
        if instance.tipo == 'gantt':
            obra.is_gantt = True
        elif instance.tipo == 'presupuesto':
            obra.is_presupuesto = True
        elif instance.tipo == 'cubicacion':
            ##AÑADIR CAMPO CUBICACION OBLIGATORIO
            pass 
        obra.save()
        
        
@receiver(post_save, sender=Obras)
def actualizar_monto_por_facturar(sender, instance, **kwargs):
    if not kwargs.get('raw', False): 
        print("dentro señal 1")
        monto_por_facturar = instance.presupuesto - instance.monto_facturado
        print(monto_por_facturar)
        Obras.objects.filter(pk=instance.pk).update(monto_por_facturar=monto_por_facturar)
    
    
@receiver(post_save, sender=Historial)
def actualizar_facturacion(sender, instance, created, **kwargs):
    print("dentro señal 2")
    if created:
        id_obra = instance.id_obra_id
        obra = Obras.objects.get(pk=id_obra)
        obra.monto_facturado = obra.monto_facturado + instance.monto
        obra.porc_avance_financiero = (obra.monto_facturado / obra.presupuesto) * 100
        obra.save()
        