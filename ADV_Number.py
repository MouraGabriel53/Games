import random

while(1):
    numGerado = random.randint(0, 10)
    num = int(input('Adivinhe o numero (0 a 10): '))

    if num == numGerado:
        print('Voce acertou! O numero escolhido pelo computador e:', numGerado)
    else:
        print('Voce errou! O numero escolhido pelo computador e:', numGerado)
        
    sair = input(str('Deseja sair (s/n): '))
    if sair == 's':
        print('Saindo...')
        break
    else:
        print('Continuando...')
    