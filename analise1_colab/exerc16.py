"""## Exercício 16: Verifique se um número é par ou ímpar usando if ternário."""

num = int(input('Digite um número: '))
print('Par' if num % 2 == 0 else 'Ímpar')

#Verifique o(s) número(s) apresentados;
#Faça a divisão de cada um por 2;
#Se o resultado for um número inteiro diga que é par;
#Se for um número decimal, que é ímpar.

num = int(input('Digite um número: '))
if num % 2 == 0:
  print('Par')
else:
  print('Ímpar')
  
