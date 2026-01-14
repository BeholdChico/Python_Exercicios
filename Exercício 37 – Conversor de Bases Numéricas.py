numero = int(input('Digite um número: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)}[2:]')
elif opcao == 2: 
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)}[2:]')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL ée igual a {hex(numero)}[2:] ')
else:
    print('Opção inválida! Tente novamente.')