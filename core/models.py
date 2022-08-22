from django.db import models


# Create your models here.
class produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return self.nome

class cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    sobrenome = models.CharField('sobrenome', max_length=50)
    email = models.EmailField('E-mail', max_length=50)

    def __str__(self):
        return  f'{self.nome} {self.sobrenome}'




