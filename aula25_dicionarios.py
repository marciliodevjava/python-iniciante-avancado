# Dicionários tem chave e  valor

meu_dicionario = {'nome': 'Ana', 'idade': 80}

print(f'Nome: {meu_dicionario["nome"]}')
print(f'Idade: {meu_dicionario["idade"]}')
print()

meu_dicionario = [
    {'nome': 'Alessandra', 'idade': 27},
    {'nome': 'Isabela', 'idade': 10},
    {'nome': 'Marcilio', 'idade': 29},
]

nome = list()
idade = list()
for i in meu_dicionario:
    print(f"Nome: {i['nome']}")
    print(f"Idade: {i['idade']}")
    nome.append(i['nome'])
    idade.append(i['idade'])
    print()

nome_tupla = tuple(nome)
idade_tupla = tuple(idade)

print(f'Tupla de nome: {nome_tupla}')
print(f'Tupla de idade: {idade_tupla}')
