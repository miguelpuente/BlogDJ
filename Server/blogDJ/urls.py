"""blogDJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from users.views import listadoUsuarios, crearUser
from blog.views import infoBlog, editarBlog
from categorias.views import listadoCategorias, crearCategoria, editarCategoria, eliminarCategoria
from posts.views import listadoPosts, crearPost, editarPost, eliminarPost

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # path('panel/', admin.site.urls),

    # Administración Blog
    path('panel/blog', infoBlog.as_view(template_name = 'blog/index.html'), name='infoblog'),
    path('panel/blog/editar/<int:pk>', editarBlog.as_view(template_name = 'blog/editar.html'), name = 'editarBlog'),

    # Administración Categorías
    path('panel/categorias', listadoCategorias.as_view(template_name = 'categorias/index.html'), name='listadodecategorias'),
    path('panel/categorias/crear', crearCategoria.as_view(template_name = 'categorias/crear.html'), name = 'crearCategoria'),
    path('panel/categorias/editar/<int:pk>', editarCategoria.as_view(template_name = 'categorias/editar.html'), name = 'editarCategoria'),
    path('panel/categorias/eliminar/<int:pk>', eliminarCategoria.as_view(), name = 'eliminarCategoria'),

    # Administración Posts
    path('panel/posts', listadoPosts.as_view(template_name = 'posts/index.html'), name='listadodeposts'),
    path('panel/posts/crear', crearPost.as_view(template_name = 'posts/crear.html'), name = 'crearPost'),
    path('panel/posts/editar/<int:pk>', editarPost.as_view(template_name = 'posts/editar.html'), name = 'editarPost'),
    path('panel/posts/eliminar/<int:pk>', eliminarPost.as_view(), name = 'eliminarPost'),


    # Administración Usuarios
    path('panel/usuarios', listadoUsuarios.as_view(template_name = 'users/index.html'), name='listadodeusers'),
    path('panel/users/crear', crearUser.as_view(template_name = 'users/crear.html'), name = 'crearUser'),

]
