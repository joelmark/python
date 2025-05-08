def saudacao():
    print("olá, mundo!")
saudacao()

def saudacao(nome):
    print(f"Olá, {nome}!")
saudacao("joão")

#esta função retorna valores usando palavra-chave return, o valor de retorno e utilizando pelo código que chama função.
def soma(a,b):
    return a+b

resultado = soma(3, 4)
print(resultado)

quadrado = lambda x: x ** 2
print(quadrado(5))

def funcao(): 
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


funcao()  # Imprime 10
funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20
print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.
