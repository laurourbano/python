preço = float(input('Qual é o preço do produto? R$'))
promoção = float(0.05)
desconto = float(preço * promoção)
print('Preço: R$'f'{preço:.2f}.\nPromoção: 'f'{promoção*100:.0f}% de desconto.\nDesconto: 'f'{desconto:.2f}')
print('O produto que custava R$'f'{preço:.2f}, na promoção com desconto de 'f'{promoção*100:.0f}% vai custar R$'f'{preço - desconto:.2f}')