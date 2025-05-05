"""## Exercício 14: Crie um menu onde o usuário pode escolher entre exibir a data, hora ou sair."""

from datetime import datetime, time, date

op = input('1-Data\n2-Hora\n3-Sair\nEscolha uma das opções: ')
print({
    '1': datetime.now().date(),
    '2': datetime.now().time(),
    '3': 'Saindo'

    }.get(op, 'Opção inválida'))

from datetime import datetime, time, date
hora = input('Digite um número')
{
    'hora': datetime.now().time(),
    'data': datetime.now().date(),
    'sair': f'saindo do programa'
}
 print(hora.get('hora','não encontrado'))
