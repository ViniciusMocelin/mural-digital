from django.db import models
from django.contrib.auth.models import User

class PostagemMural(models.Model):
    CORES_CHOICES = [
        ('#E3F2FD', 'Azul Suave'),
        ('#E8F5E9', 'Verde Suave'),
        ('#FFFDE7', 'Amarelo Suave'),
        ('#FFEBEE', 'Vermelho Suave'),
        ('#F3E5F5', 'Roxo Suave'),
    ]

    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    titulo = models.CharField(max_length=100, verbose_name="Título do Card")
    conteudo = models.TextField(verbose_name="Conteúdo da Mensagem")
    cor_fundo = models.CharField(max_length=7, choices=CORES_CHOICES, default='#E3F2FD', verbose_name="Cor do Card")
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    class Meta:
        ordering = ['-data_criacao']
        verbose_name = "Postagem do Mural"
        verbose_name_plural = "Postagens do Mural"

    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"