from django.shortcuts import render, redirect
from .forms import UsuarioRegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UsuarioRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro concluído com sucesso! Faça login.')
            return redirect('login')  # Certifique-se de que a URL 'login' esteja configurada
        else:
            messages.error(request, 'Erro no registro. Verifique os dados informados.')
    else:
        form = UsuarioRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
