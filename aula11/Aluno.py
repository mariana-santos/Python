class Aluno:
    def __init__(self, nome, idade, ra, curso):
        self.__nome = nome
        self.__idade = idade
        self.__ra = ra
        self.__curso = curso

    def get_nome (self):
        return self.__nome
    
    def set_nome (self, nome):
        self.__nome = nome

    def get_idade (self):
        return self.__idade
    
    def set_idade (self, idade):
        self.__idade = idade

    def get_ra (self):
        return self.__ra
    
    def set_ra (self, ra):
        self.__ra = ra

    def get_curso (self):
        return self.__curso
    
    def set_curso (self, curso):
        self.__curso = curso