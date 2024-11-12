from django.shortcuts import render, redirect
from .forms import UsuarioRegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UsuarioRegistrationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)  # Não salva ainda para configurar a senha
            usuario.set_password(form.cleaned_data['senha'])  # Configura a senha
            usuario.save()
            messages.success(request, 'Registro concluído com sucesso! Faça login para continuar.')
            return redirect('login')  # Redireciona para a página de login
    else:
        form = UsuarioRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
