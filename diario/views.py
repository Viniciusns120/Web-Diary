from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa, Diario
from datetime import datetime, timedelta
from django.contrib import messages


# Create your views here.
def home(request):
    textos = Diario.objects.all().order_by('create_at')[:3]
    pessoas = Pessoa.objects.all()

    # first graphic
    nomes = [pessoa.nome for pessoa in pessoas] # X axis for graphic
    qtds = []  
    for pessoa in pessoas:
        qtd = Diario.objects.filter(pessoas=pessoa).count() # Y axix for graphic
        qtds.append(qtd) 



    return render(request, 'home.html', {'textos': textos, 'nomes': nomes, 'qtds': qtds})

def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        return render(request, 'escrever.html', {'pessoas': pessoas})
    
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')

        if len(titulo.strip()) == 0 or len(texto.strip()) == 0:
            #todo: adicionar mensagem de erro
            messages.error(request, 'Preencha todos os campos para continuar')
            return redirect('escrever')

        diario = Diario(
            titulo = titulo,
            texto = texto
        )
        diario.set_tags(tags)
        diario.save()

        for i in pessoas:
            pessoa = Pessoa.objects.get(id=i)
            diario.pessoas.add(pessoa)

        diario.save()
        
        # todo mensagem de sucesso
        messages.success(request, 'Sua anotação foi salva com sucesso')
        return redirect('escrever')

def cadastrar_pessoa(request):
    if request.method == 'GET':
        return render(request, 'pessoa.html')

    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')

        pessoa = Pessoa (
            nome = nome,
            foto = foto
        )
        pessoa.save()
        return redirect('escrever')

def dia(request):
    data = request.GET.get('data')
    data_formatada = datetime.strptime(data, '%Y-%m-%d')
    diarios = Diario.objects.filter(create_at__gte=data_formatada).filter(create_at__lte=data_formatada+timedelta(days=1))

    return render(request, 'dia.html', {'diarios': diarios, 'total': diarios.count(), 'data': data})

def excluir_dia(request):
    dia = datetime.strptime(request.GET.get('data'), '%Y-%m-%d')
    diarios = Diario.objects.filter(create_at__gte=dia).filter(create_at__lte=dia+timedelta(days=1))
    messages.warning(request, 'Você tem certeza que deseja fazer isso?')
    diarios.delete()
    return HttpResponse('teste')

