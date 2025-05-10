# # Lista
# estados_lista = ['SP','RJ','MG']
# print(estados_lista[1]) #RJ
# estados_lista[1] = 'SC'
# print(estados_lista)  #SC
# estados_lista.append('AC')
# print(estados_lista) # SP,SC,MG,AC
# estados_lista.insert(2, 'ES')
# print(estados_lista) # SP,SC,ES,MG,AC
# estados_lista.remove('SP')
# print(estados_lista) #SC,ES,MG,AC
# estados_lista.pop(1)
# print(estados_lista) #SC,MG,AC

# # Tupla - coordenadas, dias da semana, meses...
# estados_tupla = ('SP','RJ','RJ')
# print(estados_tupla[1]) #RJ
# estados_tupla[1] = 'SC' #ERRO - Tuplas são imutáveis
# estados_tupla.append('SC') #ERRO
# estados_tupla.remove('SP') #ERRO

# # Set
# estados_set = {'SP','RJ','MG'}
# print(estados_set[1]) #ERRO
# estados_set.add('SC') #SP,SC,RJ,MG
# estados_set.add('RJ') 
# estados_set.remove('SP') #RJ,SC,MG

# # Dicionário
# estados_dict = {'SP': 'São Paulo','RJ': 'Rio de Janeiro','MG': 'Minas Gerais'}
# print(estados_dict['RJ']) #Rio de Janeiro
# estados_dict['RJ'] = 'RioJaneiro' 
# print(estados_dict) # {'SP': 'São Paulo','RJ': 'RioJaneiro','MG': 'Minas Gerais'}
# estados_dict['nome'] = 'Ana'
# print(estados_dict) # {'SP': 'São Paulo','RJ': 'RioJaneiro','MG': 'Minas Gerais', 'nome', 'Ana'}
# del estados_dict['MG']

# # 1- Armazene 5 frutas nas 4 estruturas.
# # - Array (usar lista mesmo)
# lista = []
# # - estrutura de repetição
# #laço for pra preencher as frutas

frutas = []

for i in range(5):
    frutas_lista = input(f'Digite a {i+1}ª fruta: ')
    frutas.append(frutas_lista)
print(f'Lista de frutas: {frutas}')

# # - armazenamento (lista, tupla, set, dict)

frutas_lista = list(frutas)
tupla = tuple (frutas)
conjunto = set (frutas)
dicionário = dict(frutas) # ERRO dicionário precisa de dois elementos para chave/valor
dicionário2 = {j: valor for j, valor in enumerate(frutas)}

# # # - print

print('Lista: ', frutas_lista)
print('Tupla: ', tupla)
print('Conjunto: ', conjunto)
#print('Dicionário: ', dicionário)
print('Dicionário 2: ', dicionário2)

# # 2 - Faça o mesmo que o exercício anterior, mas com valores randômicos do tipo inteiro.
# # - faça o import random


# import random

# def gerar_dados(qtd, min_val, max_val):
#     return [random.randint(min_val, max_val) for _ in range(qtd)]

# print('Lista aleatória:\n')
# dados = gerar_dados(5,10,99)
# lista = list(dados)
# tupla = tuple(dados)
# conjunto = set(dados)
# dicionário = {j: valor for j, valor in enumerate(dados)}

# print('Lista: ',lista)
# print('Tupla: ',tupla)
# print('Conjunto: ',conjunto)
# print('Dicionário: ',dicionário)



# ################################# Lista, Tupla, Set, Dicionário
# # - Acesso por índice: Lista, Dicionário, Tupla.
# # - Alterável: Lista, Dicionário, Set.
# # - Permite duplicados: Lista, Tupla.
# # - Ordenado: Lista, Dicionário, Tupla.

# # - X
# lista2 = ['maçã', 'banana', 'uva']

# # - Y
# tupla2 = ('maçã', 'banana', 'uva')

# # = W
# conjunto2 = {'maçã', 'banana', 'uva'}

# # = Z
# dicionario3 = {'nome': 'João', 'idade': 30, 'cidade': 'SP'}

# Lista

# frutas_lista = []
# print("# Lista")
# for i in range(5):
#     nome = input(f"Digite a fruta {i + 1}°: ")
#     frutas_lista.append(nome)
# print(f"frutas_lista: {frutas_lista}\n")

#frutas_lista = ['maçã', 'banana', 'uva']
#print(frutas_lista[1])
#frutas_lista[1]
#print(frutas_lista)
#frutas_lista.append('uva')
#print(frutas_lista)
#frutas_lista.insert(2, 'manga')
#print(frutas_lista)
#frutas_lista.remove('maçã')
#print(frutas_lista)
#frutas_lista.pop(1)
#print(frutas_lista)

