#neste prorama vamos importar as funcoes do arquivo operaçoes e utilidades
#para compor o prorama principal

import operaçoes
import utilidades

resultado = operaçoes.somar(5,3)
utilidades.imprimir_mensagem(f"O resultado da soma é:{resultado}")

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f"Olá,{nome}!")