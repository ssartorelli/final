from django.db import models

# Create your models here.
class Editor(models.Model):
    nombre = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=40)
    estado = models.CharField(max_length=30)
    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'Editores'
    def __str__(self):
        return self.nombre
    
class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    class Meta:
        ordering = ['apellido']
        verbose_name_plural = 'Autores'
    def __str__(self):
        return self.nombre
        
class Libro(models.Model):
    titulo = models.CharField(max_length=30)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
    def nombre_y_apellido(self):
        return ", " .join([Autor.nombre for Autor in self.autores.all()]+[Autor.apellido for Autor in self.autores.all()])
    
    class Meta:
        ordering = ['titulo']
        verbose_name_plural = 'Libros'