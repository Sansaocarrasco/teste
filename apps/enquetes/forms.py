from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório. Insira um e-mail válido.')
    telefone = forms.CharField(max_length=15, required=False, help_text='Opcional. Insira seu telefone.')
    is_vendedor = forms.BooleanField(required=False, help_text='Marque se você é vendedor.')

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'is_vendedor', 'password1', 'password2']

    def save(self, commit=True):
        # Salvar os dados do usuário no modelo Usuario
        user = super().save(commit=False)
        usuario = Usuario(
            nome=self.cleaned_data['nome'],
            email=self.cleaned_data['email'],
            telefone=self.cleaned_data['telefone'],
            is_vendedor=self.cleaned_data['is_vendedor']
        )
        if commit:
            user.save()  # Salva o objeto User
            usuario.save()  # Salva o objeto Usuario
        return usuario
