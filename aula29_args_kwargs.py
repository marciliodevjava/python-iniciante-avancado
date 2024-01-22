# Args e Kwargs
# Args ==> Argumentos

def meu_metodo(arg1, arg2):
    return arg1 + arg2


def minha_lista_soma(list):
    return sum(list)


def soma_simplificada(*args):
    return sum(args)


def metodo_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


print(f' Meu_metodo: {meu_metodo(2, 2)}')
print(f' Minha_lista_soma: {minha_lista_soma([2, 5, 2, 3])}')
print(f' Soma_simplificada *args: {soma_simplificada(2, 3, 6, 2, 3, 3, 2)}')
print(f' Soma_simplificada **kwargs: {metodo_kwargs(2, 3, 6, 2, nome="joão", idade=3)}')

# Kwargs ==> Keyword arguments (argumentos de palavras chaves)
