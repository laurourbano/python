largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = float(largura * altura)
print('\nSua parede tem a dimensão 'f'{largura:.2f}x'f'{altura:.2f} e sua área é de 'f'{area:.2f}m².\nPara pintar essa parede, você precisará de 'f'{area / 2:.2f}l de tinta.\n\nObrigado por utilizar este programa!\n')