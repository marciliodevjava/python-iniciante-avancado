# Classes e ObjetosHerança


class Funcionario():
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def atualiza_nome(self, nome: str):
        self.__nome = self.verificar_nome_valido(nome)

    def dados(self):
        return f'\nNome: {self.__nome} \n' \
               f'Salário: {self.__salario}'

    def verificar_nome_valido(self, nome):
        if nome == str(nome):
            if len(nome) >= 0:
                return nome
            else:
                return print('Nome inválido!')
        else:
            return print('Nome inválido!')

class Administrador(Funcionario):
    def __init__(self, nome, salario, cargo):
        super().__init__(nome, salario)
        self.__cargo = cargo

    def dados(self):
        return f'{super().dados()} \nCargo: {self.__cargo}'


fabio = Funcionario('Fábio', 1430)
print(fabio.dados())
pedro = Administrador('Pedro', 1403, 'Analista')
print(pedro.dados())
fabio.atualiza_nome('Fábio Guerra')
print(fabio.dados())
pedro.atualiza_nome('Pedro Anthunes Henrique')
print(pedro.dados())
