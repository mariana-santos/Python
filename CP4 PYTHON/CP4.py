import requests

# url = "https://sujeitoprogramador.com/r-api/?api=filmes"
# response = requests.get(url, verify=False, headers={"User-Agent": "XY"})
filmes = [{"id":123,"nome":"Vingadores Ultimato","sinopse":"Ap\u00f3s Thanos eliminar metade das criaturas vivas, os Vingadores precisam lidar com a dor da perda de amigos e seus entes queridos. Com Tony Stark (Robert Downey Jr.) vagando perdido no espa\u00e7o sem \u00e1gua nem comida, Steve Rogers (Chris Evans) e Natasha Romanov (Scarlett Johansson) precisam liderar a resist\u00eancia contra o tit\u00e3 louco.","foto":"https:\/\/sujeitoprogramador.com\/r-api\/img\/filme0.png"},{"id":546,"nome":"Shazam!","sinopse":"Billy Batson (Asher Angel) tem apenas 14 anos de idade, mas recebeu de um antigo mago o dom de se transformar num super-her\u00f3i adulto chamado Shazam (Zachary Levi). Ao gritar a palavra SHAZAM!, o adolescente se transforma nessa sua poderosa vers\u00e3o adulta para se divertir e testar suas habilidades. Contudo, ele precisa aprender a controlar seus poderes para enfrentar o malvado Dr. Thaddeus Sivana (Mark Strong).","foto":"https:\/\/sujeitoprogramador.com\/r-api\/img\/filme1.png"},{"id":125,"nome":"O Primeiro Homem","sinopse":"A vida do astronauta norte-americano Neil Armstrong (Ryan Gosling) e sua jornada para se tornar o primeiro homem a andar na Lua. Os sacrif\u00edcios e custos de Neil e toda uma na\u00e7\u00e3o durante uma das mais perigosas miss\u00f5es na hist\u00f3ria das viagens espaciais.","foto":"https:\/\/sujeitoprogramador.com\/r-api\/img\/filme3.png"},{"id":400,"nome":"Mission: Impossible \u2013 Fallout","sinopse":"Obrigado a unir for\u00e7as com o agente especial da CIA August Walker (Henry Cavill) para mais uma miss\u00e3o imposs\u00edvel, Ethan Hunt (Tom Cruise) se v\u00ea novamente cara a cara com Solomon Lane (Sean Harris) e preso numa teia que envolve velhos conhecidos movidos por interesses misteriosos e contatos de moral duvidosa.","foto":"https:\/\/sujeitoprogramador.com\/r-api\/img\/filme4.png"},{"id":554,"nome":"The Meg","sinopse":"Na fossa mais profunda do Oceano Pac\u00edfico, a tripula\u00e7\u00e3o de um submarino fica presa dentro do local ap\u00f3s ser atacada por uma criatura pr\u00e9-hist\u00f3rica que se achava estar extinta, um tubar\u00e3o de mais de 20 metros de comprimento, o Megalodon. ","foto":"https:\/\/sujeitoprogramador.com\/r-api\/img\/filme5.png"},{"id":987,"nome":"Venom","sinopse":"San Francisco, Estados Unidos. Eddie Brock (Tom Hardy) \u00e9 um jornalista investigativo, que tem um quadro pr\u00f3prio em uma emissora local. Um dia, ele \u00e9 escalado para entrevistar Carlton Drake (Riz Ahmed), o criador da Funda\u00e7\u00e3o Vida, que tem investido bastante em miss\u00f5es espaciais de forma a encontrar poss\u00edveis usos medicinais para a humanidade. ","foto":"https:\/\/sujeitoprogramador.com\/r-api\/img\/filme6.png"},{"id":700,"nome":"Pacific Rim: A Revolta","sinopse":"Filho de Stacker Pentecost (Idris Elba), respons\u00e1vel pelo comando do programa Jaeger, Jake (John Boyega) era um promissor talento do programa de defesa, mas abandonou o treinamento e entrou no mundo do crime ao vasculhar ferros-velhos em busca de pe\u00e7as de rob\u00f4s abandonados.","foto":"https:\/\/sujeitoprogramador.com\/r-api\/img\/filme7.png"}]

comentarios = []

def oferece_opcoes():
    print('\nEscolha uma opção:')
    print('1 - Ver detalhes do filme')
    print('2 - Fazer um comentário do filme')
    print('3 - Excluir um comentário')
    print('4 - Sair')

def detalhes_filme(id):
    for filme in filmes:
        if(filme["id"] == id):
            print(f'\nSinopse de {filme["nome"]}: ')
            print(filme["sinopse"])

def novo_comentario(nome, comentario, id):
    id_coment = len(comentarios) + 1

    comentario = {"id": id_coment, "nome": nome, "comentario": comentario, "id_filme": id}
    comentarios.append(comentario)


def excluir_comentario(id):
    # print(len(comentarios), id)
    if(len(comentarios) >= id):
        comentarios.pop(id)
        return True
    else:
        return False

def valida_id_filme(id):
    for filme in filmes:
        if(filme["id"] == id):
            return True
    
    return False

def mostrar_comentarios(id):
    comentarios_filtrados = []

    for comentario in comentarios:
        if(comentario["id_filme"] == id):
            comentarios_filtrados.append(comentario)

    nome_filme = ''

    for filme in filmes:
        if(filme["id"] == id):
            nome_filme = filme["nome"]

    if(len(comentarios_filtrados) > 0):
        print(f'\nComentários do filme {nome_filme}:')
        for comentarios_filtrados in comentarios_filtrados:
            print(f'{comentarios_filtrados["id"]} - {comentarios_filtrados["nome"]}: {comentarios_filtrados["comentario"]}')
    else:
        print(f'{nome_filme} não possui comentários.')


for filme in filmes:
    print(f'{filme["id"]} - {filme["nome"]}')

oferece_opcoes()
opcao = int(input())

while(opcao <= 3):
    id = int(input('Digite o id do filme desejado: '))
    filme_valido = valida_id_filme(id)

    while not (filme_valido):
        id = int(input('Id inválido. Digite outro id do filme desejado: '))
        filme_valido = valida_id_filme(id)

    if(opcao == 1):
        detalhes_filme(id)
        mostrar_comentarios(id)

    elif(opcao == 2):
        nome = input('Por favor, digite o seu nome: ')
        while(nome == ''):
            nome = input('Nome é um campo obrigatório. Digite novamente: ')
        
        comentario = input('O que você tem a comentar sobre o filme? ')
        while(comentario == ''):
            comentario = input('Comentário é um campo obrigatório. Digite novamente: ')

        novo_comentario(nome, comentario, id)

        print('Comentário incluído com sucesso!')

    else:
        mostrar_comentarios(id)
        id_coment = int(input('\nPor favor, digite o id do comentário que deseja excluir: '))

        comentario_valido = excluir_comentario(id_coment - 1)

        while not comentario_valido:
            id_coment = int(input('Comentário não encontrado. Por favor, digite outro id: '))

        print('Comentário excluído com sucesso!')

    oferece_opcoes()
    opcao = int(input())