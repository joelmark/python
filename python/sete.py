#para criar um conjunto, utilize chaves ou função set()

frutas = {"maçã", "banana", "laranja"}
numeros = set([1, 2, 3, 4, 5])

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

união = conjunto1 | conjunto2
print(união)

interseção = conjunto1 & conjunto2
print(interseção)

diferença = conjunto1 - conjunto2
print (diferença)

diferença_simetrica = conjunto1 ^ conjunto2
print(diferença_simetrica)

print("exit")

frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()