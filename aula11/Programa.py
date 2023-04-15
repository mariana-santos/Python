from Aluno import Aluno

alunos = []

def oferece_opcoes():
    print('\nEscolha uma opção:')
    print('1 - Cadastrar novo aluno')
    print('2 - Alterar dados de cadastro de algum aluno')
    print('3 - Excluir dados de cadastro e algum aluno')
    print('4 - Exibir alunos cadastrados')
    print('5 - Sair')

# retorna um objeto do tipo aluno para cadastro e alteração
def set_aluno():
    nome = input('Por favor, digite o nome: ')
    idade = int(input('Por favor, digite a idade: '))
    curso = input('Por favor, digite o curso: ')
    ra = input('Por favor, digite o ra: ')

    return(Aluno(nome, idade, ra, curso))

def exibir_alunos():
    for aluno in alunos:
        obj_aluno = {aluno['aluno']}
        print(f"{aluno['id']} - {obj_aluno.get_nome()}")

oferece_opcoes()
opcao = int(input())

while(opcao <= 4):

    if(opcao == 1):
        print('Digite os dados necessários para cadastrar um novo aluno: \n')
        aluno = set_aluno()
        alunos.append({"id": str(len(alunos)+ 1), "aluno": aluno})

    elif(opcao == 2):
        # print('Digite os dados necessários para cadastrar um novo aluno: \n')
        exibir_alunos()

    oferece_opcoes()
    opcao = int(input())