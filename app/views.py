from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    lista_usuarios = [
        {'nome': 'isa', 'matricula': '20241001', 'idade': 16, 'cidade': 'Natal'},
        {'nome': 'hemerson', 'matricula': '20241002', 'idade': 17, 'cidade': 'barcelona'},
        {'nome': 'letícia', 'matricula': '20241003', 'idade': 16, 'cidade': 'ruy barbosa'},
        {'nome': 'Laíza', 'matricula': '20241004', 'idade': 18, 'cidade': 'pedra branca'},
        {'nome': 'ana júlia', 'matricula': '20241005', 'idade': 17, 'cidade': 'riachuelo'},
    ]
    
    contexto = {
        'usuarios': lista_usuarios
    }
    return render(request, 'usuarios.html', contexto)