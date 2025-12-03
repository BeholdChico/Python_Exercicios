dias_alugado = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos KM rodados? '))
print(f'O total a pagar é R${(dias_alugado * 60) + (0.15 * km_rodados):.2f}')