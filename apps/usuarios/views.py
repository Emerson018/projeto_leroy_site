from django.shortcuts import render, redirect

from apps.usuarios.forms import LoginForms, CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth, messages


def login(request):
    #esse form passa as informacoes do form para o login
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

        usuario = auth.authenticate(
            request,
            username= nome,
            password= senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f" {nome} logado com sucesso!!")
            #da pra passar o nome assim direto pq nos ja definimos o nome de index,
            #a mesma coisa para os outros, por mais q ele nao esteja na pagina 'view.py'.
            
            return redirect('index')
        else:
            messages.error(request, "Erro ao efetuar login.")
            return redirect('login')

    #parametros = 1 = requisição. 2 = template/localizacao.
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request): 
    form = CadastroForms()

    #Pega as informações de um formulário e põe em um novo
    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid(): # aqui verifica se o 'form' é valido

             
            
            #aqui ta pegando as info, ta vindo da 'forms.py'. aqui são verificações
            nome = form["nome_cadastro"].value()
            email= form["email"].value()
            senha= form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existente!")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username= nome,
                email= email,
                password= senha
            )
            usuario.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('login')


    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('login')