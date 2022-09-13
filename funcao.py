def area(larg, comp):
    s = 0
    s = larg * comp
    print(f'A área de um terreno {largura}x{comprimento} é de {s}m2')

print(' Controle de Terrenos')
print('-'*20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura,comprimento)
