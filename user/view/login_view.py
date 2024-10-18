from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Autenticar o usuário
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            # Redirecionar para a página inicial ou outra página
            return redirect('/')
        else:
            # Se o login falhar, renderize o template com uma mensagem de erro
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    
    return render(request, 'login.html')
