from django.db import models

class Animal(models.Model):
    TIPOS = [
        ("Perro", "Perro"),
        ("Gato", "Gato"),
        ("Otro", "Otro"),
    ]

    TAMANOS = [
        ("Pequeño", "Pequeño"),
        ("Mediano", "Mediano"),
        ("Grande", "Grande"),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.TextField()
    edad = models.IntegerField()
    tamano = models.CharField(max_length=20, choices=TAMANOS)
    imagen = models.ImageField(upload_to="animales/")

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, null=True, blank=True)  


    def __str__(self):
        return f"{self.nombre} quiere adoptar a {self.animal.nombre if self.animal else 'N/A'}"
