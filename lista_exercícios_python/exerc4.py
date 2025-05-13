"""## Exercício 4: Verifique se um ano é bissexto."""

#Verifique o ano apresentado;
#Com base no histórico de anos bissextos (de 4 em 4 anos), calcule se este é um deles.

ano = int(input('Digite um ano com 4 digitos: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
  print('É bissexto')
else:
  print('Não é bissexto')