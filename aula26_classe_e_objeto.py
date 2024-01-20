# Classes e Objetos

class JogadorLoteria():
    def __init__(self, nome: str(), idade: int(), sexo: str(), numeros: list()):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.__numeros = numeros

    def soma_numeros(self):
        soma = sum(self.__numeros)
        return soma

    def retorna_numero(self):
        return self.__numeros

    def retorna_nome(self):
        return self.__nome

    def __repr__(self):
        return f'Nome: {self.__nome}, Idade: {self.__idade}'


jogador_toleria_um = {
    'nome': 'Alessadra',
    'idade': 27,
    'sexo': 'Feminino',
    'numeros': (6, 12, 32, 45, 51, 60)
}

jogador_toleria_dois = {
    'nome': 'Isabela',
    'idade': 10,
    'sexo': 'Feminino',
    'numeros': (2, 10, 13, 25, 31, 56)
}

jogador_toleria_tres = {
    'nome': 'Marcilio',
    'idade': 29,
    'sexo': 'Masculino',
    'numeros': (2, 6, 16, 32, 48, 60)
}

dicionario_jogadores = [
    jogador_toleria_um,
    jogador_toleria_dois,
    jogador_toleria_tres
]

lista_pessoa = list()

for jogador in dicionario_jogadores:
    pessoa = JogadorLoteria(jogador['nome'], jogador['idade'], jogador['sexo'], jogador['numeros'])
    numero = pessoa.soma_numeros()
    print()
    print(f'Nome: {pessoa.retorna_nome()}')
    print(f'Soma números: {numero}')
    print()
    lista_pessoa.append(pessoa)

print(lista_pessoa)
