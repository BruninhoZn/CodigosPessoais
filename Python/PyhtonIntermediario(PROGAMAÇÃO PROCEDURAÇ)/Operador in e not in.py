# nome = 'Otavio'
# print('a' in nome)
# print('z' in nome)
nome = input('Digite seu nome: ')
encontrar = input('Digite oque você deseja encontrar: ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}') 
    n = int(nome.count(encontrar))
    print(f'A letra está na posição {n}'  )
else:
    print(f'{encontrar} não esta em {nome}')
    