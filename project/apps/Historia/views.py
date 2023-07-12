from django.shortcuts import render
from .models import Personaje, Faccion

# Create your views here.
def home(request):
    registro_historias = Personaje.objects.all()
    contexto = {"historias": registro_historias}
    return render(request, "Historia/index_historia.html",contexto)