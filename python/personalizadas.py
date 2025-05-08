def funcao():
    if condicao:
        raise Exception("Descriçao do erro")

try:
    funcao()
except Exception as e:
    print (f"Erro: {str(e)}")