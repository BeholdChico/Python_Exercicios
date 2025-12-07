from random import shuffle
primeiro_aluno = input('Primeiro aluno: ')
segundo_aluno = input('Segundo aluno: ')
terceiro_aluno = input('Terceiro aluno: ')
quarto_aluno = input('Quarto aluno: ')
lista_alunos = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
print(f'A ordem de apresentação será:\n{shuffle(lista_alunos, 4)}')

