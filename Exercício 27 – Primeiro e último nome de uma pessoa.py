nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'O seu primeiro nome é {n[0]}')
print(f'O seu ultimo nome é {n[len(n) - 1]}')
