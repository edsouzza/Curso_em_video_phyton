preco = float(input('Qual o preço do produto? ') )
percentdesc = float(input('Entre com o desconto % ') )
vldesc = (preco*percentdesc/100)
novovalor=preco-vldesc
print('O produto que custava R${:.2f}, na promoção com desconto de {}% vai custar R${:.2f} '.format(preco,percentdesc,novovalor))