coordenada_x = int(input('Digite um valor para o eixo X: \n'))
coordenada_y = int(input('Digite um valor para o eixo Y: \n'))

if coordenada_x > 0 and coordenada_y >  0:
    print('Ponto no primeiro quadrante\n')
elif coordenada_x < 0 and coordenada_y > 0:
    print('Ponto no segundo quadrante\n')
elif coordenada_x < 0 and coordenada_y < 0:
    print('Ponto no terceiro quadrante\n')
elif coordenada_x > 0 and coordenada_y < 0:
    print('Ponto no quarto quadrante\n')
else:
    print('O ponto esta localizado no eixo ou origem')



