# funcao lambda
somar = lambda x,y: x + y
''' o lambda substitui 3 linhas de código  em uma
def somar(x, y):
    soma = x + y
    return soma
'''
# programa principal
x = int(input('Digite o valor de x: '))
y = int(input('Digite o valor de y: '))

# exibir o resultado
print(f'A soma de {x} e {y} é {somar(x, y)}.')