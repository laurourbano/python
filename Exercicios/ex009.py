n = int(input('Digite um número para calcular a tabuada: '))
contador = 0

while (contador >= 0) and (contador < 10):
    contador = contador + 1
    print(''f'{n} x 'f'{contador:2} = 'f'{n*contador:2} ')