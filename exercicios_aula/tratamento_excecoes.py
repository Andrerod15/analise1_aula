#try:
    # código que pode dar erro
#except:
    # código executado se houver erro
#else:
    # código executado se NÃO houver erro
#finally:
    # código executado sempre

def somar(a, b,):
    if a % 2 != 0 or b % 2 != 0:
        raise ValueError('Um dos valores é ímpar')
    if a < 0 or b < 0:
        raise ValueError('Não aceita valores negativos')
    return a + b

print(somar(32, 16,))

try:
    a = int(input('Digite o primeiro valor: '))
    b = int(input('Digite o segundo valor: '))
    resultado = somar(a,b)
except ValueError as ve:
    print('Erro: ', ve)
except Exception as e:
    print('Erro inesperado!', e)
else:
    print('Soma = ', resultado)
finally:
    print('Fim do par!')
    