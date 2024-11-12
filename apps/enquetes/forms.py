from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Obrigatório. Insira um e-mail válido.')
    nome = forms.CharField(max_length=100, required=True, help_text='Insira seu nome completo.')
    telefone = forms.CharField(max_length=15, required=False, help_text='Opcional. Insira seu telefone.')
    is_vendedor = forms.BooleanField(required=False, label='Você é vendedor?', help_text='Marque esta opção se for vendedor.')

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'is_vendedor', 'password1', 'password2']

    def save(self, commit=True):
        # Salvar os dados no modelo User e associá-los ao modelo Usuario
        user = super().save(commit=False)  # Dados do User
        user.email = self.cleaned_data['email']  # Preencher o e-mail no User
        if commit:
            user.save()
            # Criar o usuário no modelo personalizado Usuario
            Usuario.objects.create(
                nome=self.cleaned_data['nome'],
                email=self.cleaned_data['email'],
                telefone=self.cleaned_data.get('telefone', ''),  # Telefone pode ser opcional
                is_vendedor=self.cleaned_data.get('is_vendedor', False)  # Valor padrão False
            )
        return user
