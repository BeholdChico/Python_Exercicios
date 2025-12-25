numero = int(input('Informe um número: '))

print(f'Analisando o número {numero}')
print(f'Unidade: {numero // 1 % 10}\nDezena: {numero // 10 % 10}\nCentena: {numero // 100 % 10}\nMilhar: {numero // 1000 % 10}')
