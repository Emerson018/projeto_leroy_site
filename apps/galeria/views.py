#aqui ENVIA OS DADOS
from apps.galeria.models import Fotografia
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.galeria.forms import FotografiaForms


def index(request):
    #se a autenticacao nao estiver feita:
    if not request.user.is_authenticated:
        messages.error(request, "Faça login para acessar a página.")
        return redirect('login')
    #aqui ta buscando todos os itens do BD
    #se colocar um '-' na frente de 'data_fotografia', ele comeca pelo ultimo.
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    return render(request, 'galeria/index.html', {"cards": fotografias})

#
def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Faça login para pesquisar.")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)

    #request.get=representacao da url. o 2° buscar se refere ao q foi escrito
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            #busca dentro do objeto se existe algo parecido dentro da
            #pesquisa q faça sentido na busca de algo
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/index.html', {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Faça login para adicionar uma nova imagem.")
        return redirect('login')
    
    #caso seja preenchido o form, aqui salvará os dados.
    form = FotografiaForms
    if request.method == 'POST':
        #reques.FILES pega as imagens
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia Cadastrada!')
            return redirect('index')
        
    #faz a requisicao, chama 'nova_imagem.html' e cria dict com formulario
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    #buscando algo dentro de objetos do Model de fotografias
    fotografia = Fotografia.objects.get(id=foto_id)
    #aqui instancia o q foi pego pra dentro de forms
    form = FotografiaForms(instance= fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada!')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Item deletado com sucesso')
    return redirect('index')

def filtro(request, categoria):
    #filtra por categoria
    #busca dentro do model de Fotografias os objetos ordenados por fotografia filtrados por imagens publicas 
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def get_values(request):
    if not request.user.is_authenticated:
        messages.error(request, "Faça login para acessar a página.")
        return redirect('login')

    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    
    return render(request, 'galeria/get_values.html', {"cards": fotografias})
