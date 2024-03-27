from django.db import models
from datetime import date
from django.core.exceptions import ValidationError

class Ventas(models.Model):
    nombre_doc = models.CharField(max_length=255)
    num_doc = models.IntegerField()
    cod_cliente = models.CharField(max_length=255)
    nom_cliente = models.CharField(max_length=255)
    fecha = models.DateField()
    fecha_venc = models.DateField(null=True)
    desc_producto = models.TextField(null=True)
    total_detalle = models.IntegerField()
    analisis_cn = models.CharField(max_length=45)
    comentario = models.TextField(null=True)
    linea = models.IntegerField()
    empresa = models.CharField(max_length=255)
    precio_unit = models.IntegerField(null=True)
    total_neto = models.IntegerField(null=True)
    es_venta = models.IntegerField(null=True)
    
    def full_clean(self):
        super().clean()
        
        if not isinstance(self.nombre_doc, str) or self.nombre_doc == '':
            raise ValidationError(f'Nombre de Documento no valido {self.nombre_doc}')
        
        if not isinstance(self.num_doc, int) and not isinstance(self.num_doc, float):
            raise ValidationError(f'Numero de Documento no valido {self.num_doc}')
            
        if not isinstance(self.cod_cliente, str) or self.cod_cliente == '':
            raise ValidationError(f'Codigo de Cliente no valido {self.cod_cliente}')
            
        if not isinstance(self.nom_cliente, str) or self.nom_cliente == '':
            raise ValidationError(f'Nombre de Cliente no valido {self.nom_cliente}')
            
        if not isinstance(self.fecha, date):
            raise ValidationError(f'Fecha no valida - {self.fecha}')
            
        if not isinstance(self.desc_producto, str):
            raise ValidationError(f'Descripcion del producto no valido {self.desc_producto}')
            
        if not isinstance(self.total_detalle, int) and not isinstance(self.total_detalle, float):
            raise ValidationError(f'Total detalle no valido {self.total_detalle}')
            
        if not isinstance(self.analisis_cn, str) and not isinstance(self.analisis_cn, float):
            print(type(self.analisis_cn))
            raise ValidationError(f'Analisis C. Negocio no valido {self.analisis_cn}')
            
        if not isinstance(self.comentario, str) and self.comentario is not None:
            raise ValidationError(f'Comentario no valido {self.comentario}')
            
        if not isinstance(self.linea, int) and not isinstance(self.linea, float):
            raise ValidationError(f'Linea no valida {self.nombre_doc}')
            
        if not isinstance(self.empresa, str) or self.empresa == '':
            raise ValidationError(f'Empresa no valida {self.empresa}')
        
        if not isinstance(self.total_neto, int) and not isinstance(self.total_neto, float):
            raise ValidationError(f'Total neto no valido {self.total_neto}')
             