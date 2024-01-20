# Compreenção de Lista

def extrai_nome(nome, valor):
    letra_a = list()
    valor = valor.strip().lower()
    for n in nome:
        for m in n:
            if m.lower() == valor:
                letra_a.append(n.strip().capitalize())
                break
            break
    return letra_a


a = [x for x in range(5)]
print(a)
print()

for i in a:
    print(f'Lista: {i}')
    if i == 0:
        print(f'Número {i} não é IMPAR nem PAR')
    elif i % 2 == 0:
        print(f'Número PAR: {i}')
    else:
        print(f'Número IMPAR: {i}')

print()
b = [x for x in range(0, 21)]
print(f'Números: {b}')
print(f'Número {[i for i in b if i == 0]}, não é IMPAR nem PAR')
print(f'Número IMPAR {[i for i in b if not i % 2 == 0]}')
print(f'Número PAR {[i for i in b if i % 2 == 0 if i != 0]}')
print()

pessoas = ['Ana', 'AleSandRa', "bruna", 'BEAtriz', 'CamiLA', ' Caroline']

aa = 'A'
bb = 'B'
cc = 'C'

print(f'Lista de Pessoas {pessoas}')
print(f'Nome com a letra {aa} nome: {extrai_nome(pessoas, aa)}')
print(f'Nome com a letra {bb} nome: {extrai_nome(pessoas, bb)}')
print(f'Nome com a letra {cc} nome: {extrai_nome(pessoas, cc)}')
