from django.urls import path
from .views import event_list, lista_categorias, criar_categoria

urlpatterns = [
    path("", event_list, name="event_list"),           # página principal
    path("categorias/", lista_categorias, name="lista_categorias"),
    path("categorias/criar/", criar_categoria, name="criar_categoria"),
]