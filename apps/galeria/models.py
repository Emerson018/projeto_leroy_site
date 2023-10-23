#SEMPRE QNDO ALTERAR ALGO AQUI, PRECIDA FAZER 'MAKEMIGRATIONS' E 'MIGRATE'
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

#aqui tamo criando um Banco de Dados
class Fotografia(models.Model):
    #nome é uma string com charfield null


# aqui ta add uma categoria pra escolher no admin
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    #Aqui é o q acontece com cada parte do formulário
    nome = models.CharField(max_length=100,null=False,blank=False)
    legenda = models.CharField(max_length=200,null=False,blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False,blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    #True = ADM decide. False = já publica na hora
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )

    

#isso é pra retornar como pop-up no app
    def __str__(self):
        return self.nome


'''
é pra visualizar o item qndo chamado pra teste, bom para ver no terminal
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
'''