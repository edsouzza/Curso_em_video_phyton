n=int(input('Digite um número para ver sua tabuada : '))
# MINHA PRIMEIRA FORMA DE EXIBIÇÃO
# x=1
# print('===========')
# print('{} X {} = {}'.format(n,x,n*x))
# x=x+1
# print('{} X {} = {}'.format(n,x,n*x))
# x=x+1
# print('{} X {} = {}'.format(n,x,n*x))
# x=x+1
# print('{} X {} = {}'.format(n,x,n*x))
# x=x+1
# print('{} X {} = {}'.format(n,x,n*x))
# x=x+1
# print('{} X {} = {}'.format(n,x,n*x))
# x=x+1
# print('{} X {} = {}'.format(n,x,n*x))
# x=x+1
# print('{} X {} = {}'.format(n,x,n*x))
# x=x+1
# print('{} X {} = {}'.format(n,x,n*x))
# x=x+1
# print('{} X {} = {}'.format(n,x,n*x))
# print('===========')

# USANDO O LAÇO FOR FICOU MUITO MELHOR
print('='*17)
listnum=[1,2,3,4,5,6,7,8,9,10]
for num in listnum:
   print(' {:2}  X {:2} = {:2}'.format(n,num,n*num))
print('='*17)