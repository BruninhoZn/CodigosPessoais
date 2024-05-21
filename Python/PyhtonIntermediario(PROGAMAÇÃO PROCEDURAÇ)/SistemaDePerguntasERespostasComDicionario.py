from time import sleep  
import os

print()

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
            
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3x2? ',
        'respostas': {
            'a': '4',
            'b': '101',
            'c': '6',
            'd': '9',
        },
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0
for pergunta, dados_pergunta in perguntas.items():
    print(f'{pergunta}: {dados_pergunta["pergunta"]}')

    print('Respostas: ')
    for resposta, dados_resposta in dados_pergunta['respostas'].items():
        print(f'[{resposta}]: {dados_resposta}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == dados_pergunta['resposta_certa']:
        print('EHHHHHH!!! Você acertou!!!!')
        respostas_certas += 1
    else:
        print('IXXIIIII!!! Você ERROU!!!!')

    print()

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100
print(f'Você acertou {respostas_certas} respostas.')

sleep(1)
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')

sleep(1)

if respostas_certas >= 1:
    print('Parabéns você foi muito bem!')
else:
    print('Mais chance na proxima!')

print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')

sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')