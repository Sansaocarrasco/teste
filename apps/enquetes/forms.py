from django import forms
from .models import Usuario

class UsuarioRegistrationForm(forms.ModelForm):
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirmacao_senha = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'telefone', 'is_vendedor']

    def clean_confirmacao_senha(self):
        senha = self.cleaned_data.get('senha')
        confirmacao_senha = self.cleaned_data.get('confirmacao_senha')
        if senha != confirmacao_senha:
            raise forms.ValidationError('As senhas não correspondem.')
        return confirmacao_senha

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data['senha'])  # Configura a senha corretamente
        if commit:
            usuario.save()
        return usuario
