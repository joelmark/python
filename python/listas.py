# para cirar uma lista temos que encerrar os elemontos com colchetes
times = ["corinthians","santos", "palmeiras"]

#para ter ascesso aos elementos da lista utilizar oi indice dos elementos entre colchetes começam em 0.
print(times [0]) #imprime "corinthians"
print(times [1]) #imprime "santos"
print(times [2]) #imprime "palmeiras"

times = ["corinthians","santos", "palmeiras"]

# adiciona um elemnto na lista
times.append("barça")
print (times) # imprime ['corinthians', 'santos', 'palmeiras', 'barça']

#insere um elemento na posição que quiser.
times.insert(0,"Real")
print(times)

#remove a primeira ocorrência de um elemento na lista.
times.remove("palmeiras")
print(times)

#pop remove e retorna o elemento em uma posição especifica
times_removida = times.pop(1)
print(times)
print(times_removida)

#ordena os elementos da lista em ordem ascedente
times.sort()
print(times)

#inverte a ordem dos elementos na lista
times.reverse()
print(times)

