
class Filme:
    def __init__ (self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes (self):
        return self.__likes

    def dar_like (self):
        self.__likes += 1
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()
        

class Serie:
    def __init__ (self, nome, ano, temporadas):
        self.__nome = nome
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    def dar_like (self):
        self.__likes += 1

    @property
    def likes (self):
        return self.__likes

    def dar_like (self):
        self.__likes += 1
        
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')


silo = Serie('Silo', 2023, 1)
silo.dar_like()
print(f'Nome: {silo.nome} - Ano: {silo.ano} - Temporadas: {silo.temporadas} - Likes: {silo.likes}' )


    