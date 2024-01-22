# Métodos de Classes e Métodos Estáticos
from datetime import datetime


class Funcionario():
    __aumento = float()

    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def __repr__(self):
        return f'Nome: {self.__nome} \nSalário: {self.__salario}'

    def dados(self):
        return f'Nome: {self.__nome} \nSálario: {self.__salario}'

    @classmethod
    def aumento(cls, valor):
        if float(valor) >= 0.3:
            print(f'Aumento não pode ser aplicado.')
        else:
            cls.__aumento = float(valor)

    @staticmethod
    def dia_util(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        else:
            return True

    def aplicar_aumento(self):
        self.__salario = self.__salario + (self.__salario * self.__aumento)


fabio = Funcionario('Fabio', 1403)
print(fabio)
fabio.aumento(0.30)
print(fabio)
fabio.aplicar_aumento()
print(fabio)
minha_data = datetime.today().date()
print(f'é dia de semana {Funcionario.dia_util(minha_data)}')
