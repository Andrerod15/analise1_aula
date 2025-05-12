# 1- Criar lógica que verifica o saldo de uma conta corrente.

saldo1 = 5600
senha1 = 1234
conta1 = int(input('Digite sua conta: '))
if conta1 == 22454:
  senhadigitada1 = int(input('Digite sua senha: '))
  if senha1 == senhadigitada1:
    print('Seu saldo é: ', saldo1)
  else:
    print('Senha inválida')
else:
    print('Conta inválida')

    
# 2- Criar uma segunda conta corrente, para simular saque, depósito e 
# transferência.

saldo2 = 8750
senha2 = 5678
conta2 = int(input('Digite sua conta: '))
if conta2 == 23190:
  senhadigitada2 = int(input('Digite sua senha: '))
  if senha2 == senhadigitada2:
    print('Seu saldo é: ', saldo2)
  else:
    print('Senha inválida')
else:
    print('Conta inválida')


# 3- Criar um menu que permita ao usuário realizar N transações até que 
# ele opte por sair. 
# utilizar o while com menu

while True:
    print('1 = Saque, 2 = Depósito, 3 = Transferência, 4 = Sair')
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
        conta = input('Escolha sua conta - conta1 ou conta2: ')
        if conta == 'conta1':
            saque = int(input('Digite o valor a ser sacado: '))
            saldo1 -= saque
            print(f'Saque realizado! Seu saldo atual é: ', saldo1)
        if conta == 'conta2':
            saque = int(input('Digite o valor a ser sacado: '))
            saldo2 -= saque
            print(f'Saque realizado! Seu saldo atual é: ', saldo2)
    if opcao == 2:
        conta = input('Escolha sua conta - conta1 ou conta2: ')
        if conta == 'conta1':
            deposito = int(input('Digite o valor a ser depositado: '))
            saldo1 += deposito
            print(f'Depósito realizado! Seu saldo atual é: ', saldo1)
        if conta == 'conta2':
            deposito = int(input('Digite o valor a ser depositado: '))
            saldo2 -= deposito
            print(f'Depósito realizado! Seu saldo atual é: ', saldo2)
    if opcao == 3:
        conta = input('Escolha sua conta - conta1 ou conta2: ')
        if conta == 'conta1':
            transf = int(input('Digite o valor a ser transferido: '))
            saldo1 -= transf
            saldo2 += transf
            print(f'Transferência realizada!')


        


