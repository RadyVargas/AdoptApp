from django.shortcuts import render
from .models import Animal   # ⬅️ corregido
from .models import Contacto
from django.shortcuts import get_object_or_404, redirect

def inicio(request):
    mensaje = "¡Bienvenido a AdoptApp! Encuentra a tu mejor amigo peludo."
    contexto = {"mensaje": mensaje}
    return render(request, 'index.html', contexto)

def lista_animales(request):   # ⬅️ renombrado por claridad
    animales = Animal.objects.all()
    return render(request, 'lista_mascotas.html', {'animales': animales})

def animales(request):
    animales = Animal.objects.all()
    return render(request, 'animales.html', {'animales': animales})

def lista_contactos(request):
    contactos = Contacto.objects.all().order_by("-fecha")
    return render(request, "contacto.html", {"contactos": contactos})

def adoptar_animal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        correo = request.POST.get("correo")
        mensaje = request.POST.get("mensaje")

        Contacto.objects.create(
            nombre=nombre,
            correo=correo,
            mensaje=mensaje,
            animal=animal
        )
        return redirect("lista_contactos")  

    return render(request, "form_adopcion.html", {"animal": animal})