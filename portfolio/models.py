from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    resumen = models.CharField(default="Desarrollo de software", max_length=50, verbose_name="Resumen")
    description = models.TextField(verbose_name='Descripción')
    url = models.TextField()
    image = models.ImageField(verbose_name='Foto principal', upload_to='projects')
    created_at = models.DateField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
    def __str__(self):
        return self.title

class ContactRequest(models.Model):
    name = models.CharField(default='null', max_length=150, verbose_name='Nombre')
    email = models.EmailField(default='null', verbose_name="Correo eléctronico")
    title = models.CharField(default='null', max_length=150, verbose_name="Título")
    message = models.TextField(default='null', verbose_name="Mensaje")
    created_at = models.DateField(auto_now_add = True, verbose_name='Recibido el')

    class Meta:
        verbose_name = 'Solicitud de contacto'
        verbose_name_plural = 'Solicitudes de contacto'

    def __str__(self):
        return self.name
    
class Experience(models.Model):
    position = models.CharField(max_length=40, verbose_name='Cargo')
    company = models.CharField(max_length=100, verbose_name='Compañía')
    since = models.DateField(verbose_name="Desde")
    to = models.DateField(verbose_name="Hasta")
    functions = RichTextField(verbose_name="Funciones")

    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'
    
    def __str__(self):
        return self.position
    
class Certificate(models.Model):
    title = models.TextField(verbose_name="Título")
    link = models.URLField(verbose_name="Enlace")
    image = models.ImageField(verbose_name="Miniatura", upload_to='certificates')
    created_at = models.DateField(auto_now_add = True, verbose_name='Creado el')

    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'

    def __str__(self):
        return self.title
    
class ProjectImages(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    belongsTo = models.CharField(max_length=255, verbose_name='Pertenece a')
    description = models.CharField(default='null', max_length= 255, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Imagen de proyecto'
        verbose_name_plural = 'Imagenes de proyectos'

    def __str__(self):
        return self.belongsTo