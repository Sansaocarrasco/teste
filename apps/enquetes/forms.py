from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório. Insira um e-mail válido.')
    nome = forms.CharField(max_length=100, required=True, help_text='Insira seu nome completo.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        # Salvar primeiro no modelo User
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Criar uma instância do modelo Usuario vinculada ao User recém-criado
            Usuario.objects.create(
                nome=self.cleaned_data['nome'],
                email=self.cleaned_data['email'],
            )
        return user
