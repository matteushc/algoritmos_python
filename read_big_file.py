
#Codigo para ler um arquivo grande e agrupar os numeros distintos e depois contar - Desafio

from bitarray import bitarray

count_user_id = bitarray(1000000000)
count_user_id.setall(False)

with open("nome_arquivo") as infile: #Lendo o arquivo linha a linha
    for line in infile:
		sp = line.split(',') #Separando os registros pelo delimitador virgular, como exemplo 
		count_user_id[sp[0]] = 1 #Acumulando o id do cliente, caso estivesse na primeira coluna
	
print(count_user_id.count()) #Contando o total de registros
