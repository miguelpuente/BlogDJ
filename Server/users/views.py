from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import User

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

# Create your views here.

class listadoUsuarios(ListView):
    model = User

class crearUser(TemplateView):
    template_name = 'crear.html'
