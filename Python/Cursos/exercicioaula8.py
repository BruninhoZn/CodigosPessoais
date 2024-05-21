nome = str(input('Digite seu nome e Sobrenome: '))
idade = int(input('Qual é sua idade? '))
ano = int(input('Qual é seu ano de nascimento? '))
m = str(input('Digite sua altura em metros: '))

print('Então seu nome é {}, você tem {} anos, nasceu em {} e tem {} metros.'.format(nome, idade, ano, m))

if idade >= 18:
    print('Você é maior de idade, prossiga.')
else:
     print('Você é menor de idade!')
