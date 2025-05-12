#Verifique o(s) número(s) apresentados;
#Verique se há sinal de negativo(-) ou não e não é zero (0);
#Se houver e não for zero (0), diga que é positivo;
#Se não, diga que é negativo;
#Se for zero diga que é zero.
#Se for zero diga que é zero.

num = int(input('Digite um número: '))
if num > 0:
  print('Positivo')
elif num < 0:
  print('Negativo')
else:
  print('Zero')