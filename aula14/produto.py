class Produto:
    def __init__(self, nome, qtd, preco) -> None:
        self.__nome = nome
        self.__qtd = qtd
        self.__preco = preco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, self):
        self.__nome = nome

    @property
    def qtd(self):
        return self.__qtd

    @qtd.setter
    def qtd(self, qtd):
        self.__qtd = qtd

    @property 
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco