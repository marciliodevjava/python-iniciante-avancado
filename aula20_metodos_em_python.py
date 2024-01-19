# Métodos em Python

def meu_metodo():
    print('Meu metodo')


def soma_dois_numero(valor1, valor2):
    if valor1 and valor2 >= 0:
        return print(f'soma: {valor1 + valor2}')
    else:
        return 'Número inválido'


meu_metodo()
soma_dois_numero(1, 2)

a = 10
letra = 'letra'

print()
print('Inteiro: {}'.format(a))
print(f'Float: {a}')
print(letra)

lista = [1, 2, 3, 4]

print()
print(f'Lista número: {lista}')
print(f'Soma da lista: {sum(lista)}')
print('Valor menor {}'.format(min(lista)))
print(f'Valor maior {max(lista)}')
print(f'Tamanho lista {len(lista)}')
print(f'Arrendondar lista {round(10.2658, 2)}')
