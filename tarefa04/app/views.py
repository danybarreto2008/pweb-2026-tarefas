from django.shortcuts import render
from datetime import date
from .models import Tarefa

def index(request):
    tarefas = Tarefa.objects.all()
    hoje = date.today()
    
    for t in tarefas:
        t.atrasada = t.prazo < hoje and t.status != 'Concluída'
        
    total = len(tarefas)
    pendentes = sum(1 for t in tarefas if t.status == 'Pendente')
    em_andamento = sum(1 for t in tarefas if t.status == 'Em Andamento')
    concluidas = sum(1 for t in tarefas if t.status == 'Concluída')
    atrasadas = sum(1 for t in tarefas if t.atrasada)
        
    context = {
        'tarefas': tarefas,
        'hoje': hoje,
        'stats': {
            'total': total,
            'pendentes': pendentes,
            'em_andamento': em_andamento,
            'concluidas': concluidas,
            'atrasadas': atrasadas,
        }
    }
    return render(request, 'index.html', context)
