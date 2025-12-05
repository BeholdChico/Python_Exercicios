cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjcente = float(input('Comprimento do cateto adjacente: '))
soma_dos_catetos = cateto_oposto ** 2 + cateto_adjcente ** 2
hipotenusa = soma_dos_catetos ** (1/2)
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')