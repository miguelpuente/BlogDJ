from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#from django.views.decorators import login_required
#from django.utils.decorators import method_decorator

from .models import Categorias

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

# Create your views here.

class listadoCategorias(ListView):
    model = Categorias

#@method_decorator(login_required, name = 'dispatch')
class crearCategoria(SuccessMessageMixin, CreateView):
    model = Categorias
    form = Categorias
    fields = "__all__"
    success_message = "¡Categoría creada exitosamente!"

    def get_success_url (self):
        return reverse('listadodecategorias')

class editarCategoria(SuccessMessageMixin, UpdateView):
    model = Categorias
    form = Categorias
    fields = "__all__"
    success_message = "¡Categoría editada exitosamente!"

    def get_success_url (self):
        return reverse('listadodecategorias')

class eliminarCategoria(SuccessMessageMixin, DeleteView):
    model = Categorias
    form = Categorias
    fields = "__all__"

    def get_success_url (self):
        success_message = "¡Categoría eliminada exitosamente!"
        messages.success(self.request, (success_message))
        return reverse('listadodecategorias')