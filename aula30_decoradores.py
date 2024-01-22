# Decoradores
# Utilizando a lib functools
import functools


def meu_decorador(funcao):
    @functools.wraps(funcao)
    def funcao_que_roda_funcao():
        print('****** Embrulhando função no decorador!*****')
        funcao()
        print(' ******* Fechando o embrulho! *********')

    return funcao_que_roda_funcao

@meu_decorador
def minha_funcao():
    print('Eu sou uma função')


minha_funcao()
