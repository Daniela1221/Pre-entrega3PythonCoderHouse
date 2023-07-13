from django.shortcuts import render, redirect
from .models import Subscribete
from .forms import SubscribirForm

# Create your views here.
def home(request):
    if request.method == "POST":
        form = SubscribirForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Home:home")
    else:  # request.method == "GET"
        form = SubscribirForm()
    return render(request, "Subscripcion/formulario.html",{"form": form})

def subscriptores(request):
    registro_subscripcion = Subscribete.objects.all()
    contexto_subs = {"Subscriptores":registro_subscripcion}
    return render(request,"Subscripcion/index_subscripcion.html",contexto_subs)

# def crear_cliente(request):
#     if request.method == "POST":
#         form = SubscribirForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("Home:home")
#     else:  # request.method == "GET"
#         form = SubscribirForm()
#     return render(request, "Subscripcion/formulario.html", {"form": form})


