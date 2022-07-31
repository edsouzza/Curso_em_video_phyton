l=float(input('Largura da parede : '))
a=float(input('Altura da parede  : '))
area=float(l*a)
tinta=area/2
print('Sua parede tem a dimensão de {}l x {}a e sua área é de {}m2.\nPara pintar essa parede, você precisará de {}l de tinta.'.format(l,a,area,tinta))