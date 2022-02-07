real = float(input("\nQuanto dinheiro você tem na carteira? R$"))
dólar = 5.26
euro = 6.02
print('\nA cotação atual do dólar está US$'f'{dólar} e a do euro €'f'{euro}')
print('\nCom R$'f'{real:.2f} reais você pode comprar US$'f'{real / dólar:.2f} dólares ou €'f'{real / euro:.2f} euros\n\nObrigado por utilizar este programa!\n')
