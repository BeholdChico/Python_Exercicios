velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Você foi multado! Excedeu o limite de 80km/h')
    print(f'A multa vai custar R$ 7.00 por cada km acima do limite. Um total de R${(velocidade - 80) * 7:.2f}')
print('Tenha um Bom dia! Dirija com segurança!')
