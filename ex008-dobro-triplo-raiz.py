n=int(input('Digite um numero : '))
print('O dobro de {} é {}'.format(n,(n*2)))
print('O triplo de {} é {}'.format(n,(n*3)))
#
#print('A raiz quadrada de {} é {:.2f}'.format(n,(n**(1/2))))
print('A raiz quadrada de {} é {:.2f}'.format(n,(pow(n,1/2))))