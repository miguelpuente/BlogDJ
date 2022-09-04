from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Blog

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

# Create your views here.

class infoBlog(ListView):
    model = Blog

class editarBlog(SuccessMessageMixin, UpdateView):
    model = Blog
    form = Blog
    fields = "__all__"
    success_message = "¡Blog editado exitosamente!"

    def get_success_url (self):
        return reverse('infoblog')

