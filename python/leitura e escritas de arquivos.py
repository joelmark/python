#leitura de arquivos
arquivo = open("dados.txt" , "r") # abrindo o conteudo do arquivo.
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

#neste exemplo o arquivo dados.txt é aberto em modo de leitura open()
#depois foi lido pelo método read()
#armazenado na variável conteudo.
#o conteudo é mostrado na tela e o arquivo é fechado utilizando o método close().

# escrita de arquivos

arquivo = open("dados.txt", "w") # Abrindo em modo leitura "w"com a funçao open(). 
arquivo.write("olá, mundo!") #a string e escrita utilizando o metodo write().
arquivo.close() #finalmente o arquivo é fecado utilizando o metrodo close().

#utilizando a declaraçao with e é fechado automaticamente uma vez que se sai do bloco with.

with open("dados.txt", "r") as arquivo:
    conteudo = arquivo .read()
    print(conteudo)

     