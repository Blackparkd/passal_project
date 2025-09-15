# Create your views here.
from django.shortcuts import render, redirect
from .models import Evento
from .models import Categoria
from .forms import CategoriaForm

def event_list(request):
    eventos = Evento.objects.all()
    return render(request, "events/list.html", {"eventos": eventos})


def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, "events/lista_categorias.html", {"categorias": categorias})

def criar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_categorias")
    else:
        form = CategoriaForm()
    return render(request, "events/criar_categoria.html", {"form": form})