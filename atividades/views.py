from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Atividade
from .forms import AtivForm

# Create your views here.
def index(request):
    context = {
        'nome': 'Teste'
    }
    return render(request, 'content.html', context)

def ativ_list(request):
    atividades = Atividade.objects.all()
    context = {
        'atividades': atividades
    }

    return render(request, 'ativ_list.html', context)

def ativ_delete(request, ativ_id):
    atividade = get_object_or_404(Atividade, pk=ativ_id)
    try:
        atividade.delete()
        atividades = Atividade.objects.all()
        context = {
            'atividades': atividades
        }

        return render(request, 'ativ_list.html', context)
    except:
        context = {
            "msg": "Erro ao deletar a atividade"
        }
        return render(request, 'ativ_list.html', context)

def ativ_update(request, ativ_id):
    atividade = get_object_or_404(Atividade, pk=ativ_id)
    try:
        if request.method == "POST":
            form = AtivForm(request.POST, instance=atividade)
            if form.is_valid():
                form.save()
                return redirect('lista')
        else:
            form = AtivForm(instance=atividade)
            context = {
                "form": form,
                "ativ_id": ativ_id
            }
            return render(request, 'ativ_edit.html', context)
    except:
        context = {
            "msg": "Erro ao editar Atividade"
        }
        return render(request, 'ativ_list.html', context)

def ativ_read(request, ativ_id):
    atividade = get_object_or_404(Atividade, pk=ativ_id)
    context = {
        "atividade": atividade
    }
    return render(request, 'ativ_detail.html', context)

def ativ_create(request):
    if request.method == "POST":
        form = AtivForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = AtivForm()
    context = {
        "form": form
    }
    return render(request, 'ativ_create.html', context)
