valor=float(input('Digite uma distância em km : '))
#tabela de conversões => km hm dam m dm cm mm
#convertendo de m para cm          1  0  0       valor x 100
#convertendo de m para mm          1  0  0  0    valor x 1000
#print('O valor de {:.2f}mt equivale a {:.2f}cm e {:.2f}mm'.format(valor,(valor*100),(valor*1000)))

#tabela de conversões =>        km hm dam m dm cm mm
#convertendo de km para hm      1  0                   valor x 10
#convertendo de km para dam     1  0  0                valor x 100
#convertendo de km para m       1  0  0   0            valor x 1000
#convertendo de km para dm      1  0  0   0  0         valor x 10000
#convertendo de km para cm      1  0  0   0  0  0      valor x 100000
#convertendo de km para mm      1  0  0   0  0  0  0   valor x 1000000

#Segunda forma de fazer com todas as medidas
print('O valor de {:.2f}km equivale a \n'
      '{:.2f}hm \n'
      '{:.2f}dam \n'
      '{:.2f}m \n'
      '{:.2f}dm \n'
      '{:.2f}cm \n'
      '{:.2f}mm'.format(valor,(valor*10),(valor*100),(valor*1000),(valor*10000),(valor*100000),(valor*1000000)))