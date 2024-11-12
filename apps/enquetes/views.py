from django.shortcuts import render, redirect
from .forms import UserRegistrationForm  # Certifique-se de que o formulário foi criado

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após registro
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
