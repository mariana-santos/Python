from urllib import response
import requests

user = input('Digite o user do github que deseja pesquisar: ')

url = f"https://api.github.com/users/{user}"
response = requests.get(url)

while (response.status_code != 200):
    user = input('Usuário inválido. Por favor pesquise outro: ')
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url)

dados = response.json()
print(f"Nome: {dados['name']}")
print(f"Qtd. de repositórios: {dados['public_repos']}")
print(f"Qtd. de seguidores: {dados['followers']}")