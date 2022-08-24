from django.urls import path

from .views import index, contato, Produto

urlpatterns = [
    path('', index, name = 'index'),
    path('contato', contato, name='contato'),
    path('Produto/<int:pk>', Produto, name='produto')
]