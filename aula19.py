# Operadores aritmeticos

zero = 0
um = 1
dois = 2
tres = 3
quatro = 4
cinco = 5
seis = 6
sete = 7
oito = 8
nove = 9

print('Operadores aritmeticos')
# Soma
a = tres + dois
print(f'Soma: {tres} + {dois} = {a}')

# Subtração
b = dois - um
print(f'Subtração: {dois} - {um} = {b}')

# Multiplicação
c = sete * oito
print('Multiplicação: {} x {} = {}'.format(sete, oito, c))

# Divisão
d = seis / tres
print('Divisão: {} / {} = {}'.format(seis, tres, d))

# Exponenciação
e = quatro ** cinco
print('Exponenciação: {} ** {} = {}'.format(quatro, cinco, e))
print()

# Operadores de Comparação
print('Operadores de Comparação')
# Igual '=='
aa = cinco == dois
print(f'Igual: {cinco} == {dois} = {aa}')

# Diferente '!='
bb = tres != dois
print(f'Diferente: {tres} != {dois} = {bb}')

# Maior
cc = quatro > tres
print('Maior: {} > {} = {}'.format(quatro, tres, cc))

# Menor
dd = um < cinco
print('Menor: {} < {} = {}'.format(um, cinco, dd))

# Maior igual
ee = quatro >= tres
print('Maior Igual: {} >= {} = {}'.format(quatro, tres, ee))

# Menor Igual
ff = um <= cinco
print('Menor Igual: {} <= {} = {}'.format(um, cinco, ff))
print()

# Operadores Lógicos
print('Operadores Lógicos')

ab = True
ac = False

# E 'and'
print(f"Verdadeiro {ab} and {ab} = {ab and ab}")

# Ou 'or'
print(f"Verdadeiro {ab} or {ac} = {ab or ac}")

# Not
print(f"Verdadeiro {ac} not = {not ac}")
print(f"Falso {ab} not = {not ab}")
