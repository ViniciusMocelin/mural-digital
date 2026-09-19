from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import PostagemMural
from .forms import PostagemForm
from django.contrib import messages

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Autentica o usuário automaticamente após se cadastrar
            messages.success(request, '🎉 Conta criada com sucesso! Bem-vindo ao School Feed.')
            return redirect('mural_lista')
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})

def index_publico(request):
    # Recupera todos os cartões abertos no mural ordenados por data
    posts = PostagemMural.objects.all().order_by('-data_criacao')
    return render(request, 'mural/index_publico.html', {'posts': posts})

@login_required
def mural_list(request):
    meus_posts = PostagemMural.objects.filter(autor=request.user)
    return render(request, 'mural/mural_list.html', {'meus_posts': meus_posts})

@login_required
def criar_post(request):
    if request.method == 'POST':
        form = PostagemForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            messages.success(request, '✨ Card criado e publicado com sucesso!')
            return redirect('mural_lista')
    else:
        form = PostagemForm()
    return render(request, 'mural/mural_form.html', {
        'form': form, 
        'titulo_pagina': 'Criar Card no Mural',
        'is_edit': False
    })

@login_required
def editar_post(request, pk):
    post = get_object_or_404(PostagemMural, pk=pk, autor=request.user)
    if request.method == 'POST':
        form = PostagemForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, '✏️ Card atualizado com sucesso!')
            return redirect('mural_lista')
    else:
        form = PostagemForm(instance=post)
    return render(request, 'mural/mural_form.html', {
        'form': form, 
        'titulo_pagina': 'Editar Card',
        'is_edit': True
    })

@login_required
def deletar_post(request, pk):
    post = get_object_or_404(PostagemMural, pk=pk, autor=request.user)
    if request.method == 'POST':
        post.delete()
        messages.success(request, '🗑️ Card excluído com sucesso!')
    return redirect('mural_lista')