# Loop
# For significa para
# While significa enquanto

minha_string = 'olá mundo'

for i in minha_string:
    print(f'Letra: {i}')

print()
caracter = 0

while caracter <= len(minha_string):
    print(f'Letra: {minha_string[caracter]}')
    caracter += 1
    if caracter >= len(minha_string):
        print()
        break

# Cria lista com uma tamanho
# range(start, stop, step)

lista = range(0, 10, 1)

for i in lista:
    print(f'Número: {i}')

print()
print('Imprimendo ao ²')

for i in lista:
    print(f'Numero {i}² = {i ** 2}')

print()

print('Número IMPAR')
print()
for i in lista:
    if not i % 2 == 0:
        print(f'Número impar: {i}')

print()

print('Número PAR')
print()
for i in lista:
    if i % 2 == 0:
        print(f'Número par: {i}')
