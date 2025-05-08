números = [1, 2, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 ==0]
print(quadrados) 

# este exemplo foi criado um nova lista chamada quadrados , que contém os quadrados
#dos numeros pares da lista números 
# a expressão x** 2 eleva cada elemento ao quadrado.
# a condição if x % 2 == 0 filtra os numeros pares.
