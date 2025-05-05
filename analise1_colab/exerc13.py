"""## Exercício 13: Crie um programa que traduza números de 1 a 5 para palavras (1 = um, 2 = dois...)."""

def traducao(num):
  return {
      '1': "um",
      '2': "dois",
      '3': "três",
      '4': "quatro",
      '5': "cinco"

  }.get(num, 'não encontrado')

num = input('Digite um número de 1 a 5: ')
print(traducao(num))
