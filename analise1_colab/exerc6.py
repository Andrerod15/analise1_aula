"""## Exercício 6: Verifique se um usuário pode votar (idade >= 18)."""

#Verifique o número da idade realacionada ao usuário;
#Se for maior ou igual à 18, diga que pode votar;
#Se for menor que 18, diga que não pode.

num = int(input('Informe a idade: '))
if num >= 18:
  print('Pode votar')
else:
  print('Não pode votar')