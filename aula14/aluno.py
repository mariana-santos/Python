class Aluno:
    def __init__(self, nome, nota, cidade) -> None:
        self.__nome = nome
        self.__nota = nota
        self.___cidade = cidade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(nome, self):
        self.__nome = nome

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(nota, self):
        self.__nota = nota

    @property
    def cidade(self):
        return self.___cidade

    @cidade.setter
    def cidade(cidade, self):
        self.__cidade = cidade