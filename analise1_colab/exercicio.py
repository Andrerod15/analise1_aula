#Exercicio 1 
# Definir as variáveis de entrada
lar = float(input("Informe a largura do cômodo (m): "))
comp = float(input("Informe o comprimento do cômodo (m): "))
potencia_lampada = float(input("Informe a potência da lâmpada (watts): "))

# Calcular a área do cômodo
area = lar * comp

# Calcular a potência total necessária (3 watts por metro quadrado)
potencia_total = area * 3  

# Calcular o número total de lâmpadas
numero_lampadas = potencia_total / potencia_lampada

# Calcular o número de bocais
numero_bocais = area / 3  # Um bocal a cada 3 m²

# Exibir os resultados de maneira mais simples
print("Número de lâmpadas necessárias:", round(numero_lampadas))

#Exercicio 2
comprimento=float(input("Informe o comprimento do cômodo: "))
largura= float(input("Informe a largura do cômodo: "))
altura=float(input("Informe altura: "))

metrostotal= 2*(largura*comprimento) + 2*(altura*largura)
total=metrostotal/1.5

print (int("total de caixas de azulejos", total))

#exercicio 3
""" Um motorista de táxi deseja calcular o rendimento de seu carro
na praça. Sabendo-se que o preço do combustível é de R$ 4,87,
escreva um programa para ler: a marcação do odômetro (km) no
início do dia, a marcação (km) no final do dia, o número de litros
de combustível gasto e o valor total (R$) recebido dos
passageiros.
Calcular e escrever: a média do consumo em km/L e o lucro
(líquido) do dia."""




inicio_km = float(input("Digite o km odômetro no início do dia (km): "))
fim_km = float(input("Digite a km do odômetro no final do dia (km): "))
litros_gastos = float(input("Digite quantos litros de combustível gasto: "))
valor_recebido = float(input("Digite o valor total recebido dos passageiros (R$): "))

# preço do combustivel
preco_combustivel = 4.87

# Cálculos passo a paso
distancia_percorrida = fim_km - inicio_km
consumo_medio = distancia_percorrida / litros_gastos
custo_combustivel = litros_gastos * preco_combustivel
lucro_liquido = valor_recebido - custo_combustivel

# Resultados
print(f"\nMédia de consumo: {consumo_medio:.2f} km/L")
print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")