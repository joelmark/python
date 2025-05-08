# O bloco try contém um códio que pode ter exceçao
#se ter exceçao o fluxo de execuçao e tranferido para o bloco except

try: 
    resultado = 10 / 0
    print (resultado)
except ZeroDivisionError:
    print("Erro: Divisao por zero")

#Except >>> especifica o tipo de exceçao que se deseja capturar e lidar

try:
    resultado = 10 / 0
    print (resultado)
except ZeroDivisionError:
    print("Erro : Divisao por zero")
except ValueError:
    print("Erro: valor inválido")

#FINALLY >> É opcional e é excutado sempre, indepedemnte de ter ocorrido,
# uma exceçao ou nao, utilizado parafas de limpeza ou liberaçao de recursos. realizar tare

try:
    arquivo = open("arquivo.txt","r")
    #realizar operaçoes com o arquivo
except FileNotFoundError:
    print("Erro: Arquivo nao encontrado")
finally:
    arquivo.close() #fecar o arquivo sempre, mesmo se ocorrer uma exceçao.