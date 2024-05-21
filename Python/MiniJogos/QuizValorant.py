from time import sleep 
import os 

print()

perguntas = {
    'Pergunta 1': {
        'pergunta' : 'Em que ano lançou o Valorant?',
        'respostas': {
            'A': '2022',
            'B': '1924',
            'C': '2020',
            'D': '2016',
            'E': 'NDA',
            },
        'resposta_certa': 'C',
        },

    'Pergunta 2': {
        'pergunta' : 'Qual o nome da empresa que criou o valorant?',
        'respostas': {
            'A': 'Riot Games',
            'B': 'Blizzard',
            'C': 'Activison',
            'D': 'Epic Games',
            'E': 'NDA',
            },
        'resposta_certa': 'A',
    }
}
print()
sleep(2)
resposta_certas = 0
for perguntas, dados_perguntas in perguntas.items():
    print(f'{perguntas}: {dados_perguntas["pergunta"]}')
    
    print('Respostas:   ')
    sleep(1)
    for resposta, dados_respostas in dados_perguntas['respostas'].items():
        print(f'[{resposta}]: {dados_respostas}')
        
    resposta_usuario = input('Sua resposta: ')
    sleep(1)
    
    if resposta_usuario == dados_perguntas['resposta_certa']:
        print('Boaaa!! Você acertou!!!')
        resposta_certas += 1
    else:
        print('Você errou! Mais atenção na proxima!')
        
    print()
    quantidade_perguntas = len(perguntas)
porcentagem_acerto = resposta_certas / quantidade_perguntas * 100
print(f'Você acertou {resposta_certas} respostas.')

sleep(1)
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')

sleep(1)

if resposta_certas > 1:
    print('Parabéns você foi muito bem!')
else:
    print('Mais chance na proxima!')

print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%.')

sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')
    
    
    
    
    
    
    
    
