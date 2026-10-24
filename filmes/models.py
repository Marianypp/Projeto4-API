from django.db import models

class Generos(models.Model):
    nome = models.CharField(max_length=100)                         # nome do gênero
    
    def __str__(self):
       return self.nome                                             # representação em string do gênero do filme

class Filmes(models.Model):
    titulo = models.CharField(max_length=100)                       # título do filme
    descricao = models.CharField(max_length=500)                    # descrição do filme
    ano_lancamento = models.PositiveIntegerField()                  # ano de lançamento (positivo)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)   # chave esrangeira que liga à tabela gêneros. On_delete CASCADE apaga todos os filmes denro de um mesmo gênero, caso ele seja apagado.
    duracao = models.CharField(max_length=11)                       # duração do filme

    def __str__(self):
        return self.titulo                                          # representação em string do título do filme
