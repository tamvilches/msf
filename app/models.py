from django.db import models

# Create your models here.

#Clase Rol
class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    def _str_(self):
        return self.nombre
        
        
#Clase Region
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.nombre
        
#Clase Comuna        
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def _str_(self):
        return self.nombre
    
#Clase Medicamento
class Medicamento(models.Model):
    id_medicamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    medicion = models.CharField(max_length=100)
    fecha_venc = models.DateField()
    lote = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    laboratorio = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre
    
#Clase Receta
class Receta(models.Model):
    folio = models.IntegerField(primary_key=True)
    medico_asociado = models.CharField(max_length=100)

    def _str_(self):
        return self.medico_asociado

    
#Clase Persona
class Persona(models.Model):
    rut = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    cargo= models.CharField(max_length=100)

    def _str_(self):
        return self.nombre
    
#Clase Usuario
class Usuario(models.Model):
    rut = models.CharField(max_length=100, primary_key=True)
    contraseña = models.CharField(max_length=100)
    vigencia = models.CharField(max_length=100)

    def _str_(self):
        return self.rut


#Clase Paciente
class Paciente(models.Model):
    rut = models.CharField(max_length=100, primary_key=True)
    diagnostico = models.CharField(max_length=200)    
    receta= models.CharField(max_length=200)

    def _str_(self):
        return self.rut

#Clase Cesfam
class Cesfam(models.Model):
    id_cesfam = models.CharField(max_length=100, primary_key=True)
    nombre = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre  
    
#Clase Despacho
class Despacho(models.Model):
    id_despacho = models.IntegerField(primary_key=True)
    fecha = models.DateField()

    def _str_(self):
        return self.id_despacho 

#Clase Historial
class Historial(models.Model):
    id_historial = models.CharField(max_length=100, primary_key=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def _str_(self):
        return self.id_historial 