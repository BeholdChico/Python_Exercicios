casa = float(input('Informe o valor do imóvel: R$'))
salario = float(input('Me diga seu salário: R$'))
tempo = int(input('Quantos anos de financiamento? '))
prestacao = casa / (tempo * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {tempo} anos a prestação será de R${prestacao}')
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
