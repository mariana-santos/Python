class Cliente:
    def __init__(self, nome, idade, cidade) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__cidade = cidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, self):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property 
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade):
        self.__cidade = cidade