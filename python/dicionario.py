# para criar um dicionário, utilize chaves e separe as chaves e valores com dois pontos.

pessoa = {"nome":"joão","idade": 25, "cidade":"Madri"}

#Pare ter acesso os valores de um dicionário, utilize a chave correspondente entre colchetes

print(pessoa["nome"]) #imprime "joão"
print(pessoa["idade"]) #imprime 25
print(pessoa["cidade"]) #imprime "Madri"
print("fim")

#metodos para manipular e acessar os elementos

pessoa2 = {"nome": "joão", "idade": "22", "cidade": "Madri"}

#retorna uma visualização de todas as chaves do dicionário
print(pessoa2.keys())

#retorna a visualização de todos os valores do dicionario
print(pessoa2.values())

#retorna uma visualização de todos os pares chave-valor do dicionário
print(pessoa2.items())

#Atualiza a lista do dicionario 
pessoa2.update({"profissao": "engenheiro"})
print(pessoa2) 