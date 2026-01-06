from random import randint
from time import sleep
numero = randint(0 , 5) # Faz o computador 'PENSAR'
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar..')
print('-=-' * 20)
palpite = input('Em que número eu pensei? ') # Jogador tenta adivinhar
palpite_int = int(palpite) # Conversão de str para int
print('\nPensando...')
sleep(3)
if palpite_int == numero:
    print('Você acertou PARABENS!')
else:
    print('Infelizmente você errou\n')
print(f'O número escolhido foi {numero}')

