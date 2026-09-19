from django.urls import path
from . import views

urlpatterns = [
    # Rota principal do sistema (Livre acesso)
    path('', views.index_publico, name='mural_publico'),
    path('mural_list/', views.mural_list, name='mural_lista'),
    path('novo/', views.criar_post, name='criar_post'),
    path('editar/<int:pk>/', views.editar_post, name='editar_post'),
]