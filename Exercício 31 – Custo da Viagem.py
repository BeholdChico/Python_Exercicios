distancia = float(input('Qual a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia:.1f}KM.')
if distancia <= 200:
    print(f'E o preço da sua passagem será de R${0.50 * distancia:.2f}')
if distancia > 200:
    print(f'E o preço da sua passagem será de R${0.45 * distancia:.2f} ')