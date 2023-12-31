class Programa:
    def __init__(self, nome, ano, likes):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes (self):
        return self._likes

    def dar_like (self):
        self._likes += 1
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):
    def __init__ (self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
            
class Serie(Programa):
    def __init__ (self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')


silo = Serie('Silo', 2023, 1)

print(f'Nome: {silo.nome} - Ano: {silo.ano} - Temporadas: {silo.temporadas} - Likes: {silo.likes}' )


    