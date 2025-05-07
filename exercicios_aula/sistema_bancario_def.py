# 1- Criar lógica que verifica o saldo de uma conta corrente.

# 2- Criar uma segunda conta corrente, para simular saque, depósito e transferência.

# 3- Criar um menu que permita ao usuário realizar N transações até que ele opte por sair. 
# utilizar o while com menu

conta1 = 22454
saldo1 = 5600

conta2 = 23190
saldo2 = 8750

#saldo1 -= valor     # lógica do saque

#saldo1 += valor      # lógica do depósito

#saldo1 -= valor     # lógica da transferência
#saldo2 += valor

while True:
  print('1-Consultar saldo\n2-Depósito\n3-Transferência\n4-Saque\n5-Sair')
  op = int(input('Escolha uma opção: '))
  
  if op == 1:
    print(f'O saldo da conta 1 é: {saldo1}')
  elif op == 2:
    valor = float(input('Escolha o valor da saque: '))
    saldo1 += valor
    print(f'Depósito realizado com sucesso!\nO saldo da conta 1 é: {saldo1}')
  elif op == 3:
    valor = float(input('Escolha o valor da transferência: '))
    saldo1 -= valor
    saldo2 += valor
    print(f'Transferência realizada com sucesso!\nO saldo da conta 1 é: {saldo1}')
  elif op == 4:
    valor = float(input('Escolha o valor do saque: '))
    saldo1 -= valor
    print(f'Saque realizado com sucesso!\nO saldo da conta 1 é: {saldo1}')
  elif op == 5:
    print('Obrigado!')
    break

def exibir_menu():
    print('1-Consultar saldo\n2-Depósito\n3-Transferência\n4-Saque\n5-Sair')
    
def sacar(valor):
    global saldo
    saldo -= valor
    print(f'Saque realizado!\nO saldo atual da conta é: {saldo1}')

def depositar(valor):
    global saldo
    saldo += valor
    print(f'Depósito realizado!\nO saldo atual da conta é: {saldo1}')

def transferir(valor):
    global saldo, destinatario
    saldo -= valor
    destinatario += valor
    print(f'Transferência realizada!\nO saldo atual da conta é: {saldo1}')


#match/case - opção alternativa ao if/else para o uso de listas condicionais mais 
#abrangentes, de grande porte e organizadas.
