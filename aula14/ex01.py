from aluno import Aluno

alunosVestibular = "Jose dos Santos,7,Sao Paulo;Sandra Silva,6.5,Sao Jose do Rio Preto;Augusto Soares,8,Sao Paulo;Vanderlei Azevedo,5.65,Santos;Vanessa Ferreira,9,Sao Paulo;Natan Cruz,10,Sao Paulo."

alunos = alunosVestibular.split(';')

lista_alunos = {}
id = 0

for dados in alunos:
    campos = dados.split(',')

    if(float(campos[1]) >= 7):
        nome = campos[0]
        nota = campos[1]
        cidade = campos[2]
        aluno = Aluno(nome, nota, cidade)

        lista_alunos[id] = aluno
        id = id + 1


# print(lista_alunos)
for id, aluno in lista_alunos.items():
    print(f'Nome: {aluno.nome}')
    print(f'Nota: {aluno.nota}')
    print(f'Cidade: {aluno.cidade} \n')