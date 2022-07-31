real=float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar=4.76
print('Com R${} você pode comprar US${:.2f}'.format(real, real / dolar))