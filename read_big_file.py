
#Codigo para ler um arquivo grande e agrupar os numeros distintos e depois contar - Desafio

#Primeiro iria ler o arquivo linha por linha sem carregar na memória. Durante a leitura iria registrar o id do cliente
#em um conjunto (set), pois guarda somente os numeros únicos,  e depois iria contar a quantidade de registros acumulados 
#nesse conjunto.

from bitarray import bitarray

count_user_id = bitarray(1000000000)
count_user_id.setall(False)

with open("nome_arquivo") as infile: #Lendo o arquivo linha a linha
    for line in infile:
		sp = line.split(',') #Separando os registros pelo delimitador virgular, como exemplo 
		count_user_id[sp[0]] = 1 #Acumulando o id do cliente, caso estivesse na primeira coluna
	
print(count_user_id.count()) #Contando o total de registros
