# MATH>>> fornecer funçoes matematicas
# RADOM>>  oferece funcoes para erar numeros aleatorio
# DATETIME >> permitir trabalhar com datas e horas.

import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime um número inteiro aleatório entre 1 e 10


data_atual = datetime.datetime.now()
print(data_atual)  # Imprime a data e hora atual