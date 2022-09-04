from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Posts

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

# Create your views here.

class listadoPosts(ListView):
    model = Posts

class crearPost(SuccessMessageMixin, CreateView):
    model = Posts
    form = Posts
    fields = "__all__"
    success_message = '¡Post creado exitosamente!'

    def get_success_url (self):
        return reverse('listadodeposts')

class editarPost(SuccessMessageMixin, UpdateView):
    model = Posts
    form = Posts
    fields = "__all__"
    success_message = '¡Post editado exitosamente!'

    def get_success_url (self):
        return reverse('listadodeposts')

class eliminarPost(SuccessMessageMixin, DeleteView):
    model = Posts
    form = Posts
    fields = "__all__"

    def get_success_url (self):
        success_message = '¡Post eliminado exitosamente!'
        messages.success(self.request, (success_message))
        return reverse('listadodeposts')