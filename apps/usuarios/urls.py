#URLS DO USUARIOS

from  django.urls import path
from apps.usuarios.views import login, cadastro, logout

#boas praticas. aqui só tem URLS se essas paginas forem relacionadas a GALERIA.
urlpatterns = [
    #parametros: 1 = caminho. 2 = nome do metodo chamado 3 = referência 
    path('login', login, name= 'login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),

]