# If significa Se
# Else significa Se não

a = 1
b = 2

if a >= 0:
    print(f'Valor maior que 0, valor: {a}')
else:
    print(f'Valor não é maior que zero')

if b >= 0:
    print(f'Valor maior que 0, valor: {b}')
else:
    print(f'Valor não é maior que zero')

devo_continuar = True
devo_parar = False

if devo_continuar:
    print('Verdadeiro')
    if devo_parar:
        print('Verdadeiro')
    else:
        print('Falso')

pessoas = ['Paulo', 'Bruno', 'Camargo']
# Convertendo todas as strings da lista para maiúsculas
pessoas_upper = [p.upper() for p in pessoas]

pessoa = str(input('Digite um nome: '))

if pessoa.upper() in pessoas_upper:
    print(f'A {pessoa}, está na lista')
else:
    print(f'A {pessoa}, não na lista')

pessoa += ' Você não conhece'
print(pessoa)