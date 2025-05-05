"""## Exercício 12: Crie um menu para converter temperaturas entre Celsius, Fahrenheit e Kelvin."""

def conversao(t,temp):
  return {
      'F': (temp *9/5) +32 ,
      'K': (temp + 273)

  }.get(t,'Conversão não encontrada')

t = input('Digite a escala de temperatura F/K: ')
temp = float(input('Digite o valor da temperatura: '))
print(conversao(t,temp))