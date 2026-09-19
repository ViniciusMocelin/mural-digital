from django import forms
from .models import PostagemMural

class PostagemForm(forms.ModelForm):
    class Meta:
        model = PostagemMural
        fields = ['titulo', 'conteudo', 'cor_fundo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'glass-input', 
                'placeholder': 'Título do seu post...'
            }),
            'conteudo': forms.Textarea(attrs={
                'class': 'glass-input', 
                'rows': 4, 
                'placeholder': 'Escreva a sua mensagem...'
            }),
            'cor_fundo': forms.Select(attrs={
                'class': 'glass-input'
            }),
        }