from django.shortcuts import render, redirect
from .forms import UsuarioRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UsuarioRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados no modelo Usuario
            return redirect('login')  # Redireciona para a página de login após registro
    else:
        form = UsuarioRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
