"""## Exercício 7: Verifique se já posso ir embora da aula de Análise de Dados sem assinar a folha."""

#Verique que horas são;
#Verifique se tenho alguma urgência;
#Verifique se não tenho nada a perder;
#se for mais de 22h, diga que posso ir;
#se não for, diga que não posso;

from datetime import datetime, time

print(datetime.now().time())
if datetime.now().time() >= time(00,45,0):
  print('Pode')
else:
  print('Não pode')
  