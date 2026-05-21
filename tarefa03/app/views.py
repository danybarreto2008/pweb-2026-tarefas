from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    
    lista_usuarios = [
        {'nome': 'isa', 'matricula': '202301', 'idade': 15, 'cidade': 'natal'},
        {'nome': 'hemerson', 'matricula': '202302', 'idade': 18, 'cidade': 'barcelona'},
        {'nome': 'ana júlia', 'matricula': '202303', 'idade': 17, 'cidade': 'riachuelo'},
        {'nome': 'letícia', 'matricula': '202304', 'idade': 17, 'cidade': 'ruy barbosa'},
        {'nome': 'laíza', 'matricula': '202305', 'idade': 16, 'cidade': 'pedra branca'},
    ]
    
    context = {
        'usuarios': lista_usuarios
    }
    return render(request, 'usuarios.html', context)
