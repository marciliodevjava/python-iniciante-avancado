# Listas segue sequencia de ordenação de acordo com a add nela

numero = [1, 2, 3, 6]
print(f'Lista: {numero}')
numero.append(5)
print('Lista: ', numero)
numero.pop()
numero.pop()
print('Lista: ', numero)

# Tupla () valor da tupla imutavel

tupla_numero = (1, 2, 3, 1)
print(f'Tupla: {tupla_numero}')
tupla_numero += (5, 8, 9)
print(f'Tupla: {tupla_numero}')

# Set não pode ter valor duplicado são desrdenado

set_numero = {1, 21, 3}
print(f'Set: {set_numero}')
set_numero.update([2, 5, 6, 3])
print(f'Set: {set_numero}')
set_numero = set_numero.union({2, 15, 6, 1})
print(f'Set: {set_numero}')
